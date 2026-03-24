from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup


DUO_AMOUNTS_URL_EN = "https://duo.nl/particulier/student-finance/amounts.jsp"
# The Dutch page exists but its structure changes more often; the EN page is stable and contains the same numbers.
DUO_AMOUNTS_URL_NL = DUO_AMOUNTS_URL_EN


@dataclass
class CachedDoc:
    fetched_at: int
    url: str
    data: dict[str, Any]


class DuoAmountsClient:
    def __init__(self, cache_path: str = "./data/cache_duo_amounts.json", ttl_seconds: int = 24 * 3600) -> None:
        self.cache_path = Path(cache_path)
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_seconds

    def _read_cache(self) -> CachedDoc | None:
        if not self.cache_path.exists():
            return None
        try:
            raw = json.loads(self.cache_path.read_text(encoding="utf-8"))
            return CachedDoc(fetched_at=int(raw["fetched_at"]), url=str(raw["url"]), data=dict(raw["data"]))
        except Exception:
            return None

    def _write_cache(self, doc: CachedDoc) -> None:
        tmp = self.cache_path.with_suffix(".tmp")
        tmp.write_text(
            json.dumps({"fetched_at": doc.fetched_at, "url": doc.url, "data": doc.data}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        os.replace(tmp, self.cache_path)

    async def get_amounts(self, locale: str | None = "nl-NL", force_refresh: bool = False) -> dict[str, Any]:
        cached = self._read_cache()
        now = int(time.time())
        if cached and not force_refresh and now - cached.fetched_at < self.ttl_seconds:
            return cached.data

        url = DUO_AMOUNTS_URL_NL if (locale or "").lower().startswith("nl") else DUO_AMOUNTS_URL_EN
        data = await _fetch_and_parse(url)
        self._write_cache(CachedDoc(fetched_at=now, url=url, data=data))
        return data


def _parse_money(text: str) -> float | None:
    # Handles "€107.26" and "€1,050.08" and "€130,21" etc.
    t = text.strip()
    t = t.replace("€", "").replace("\xa0", " ").strip()
    t = re.sub(r"[^\d,.\-]", "", t)
    if not t:
        return None
    # If both comma and dot exist, assume comma is thousands separator.
    if "," in t and "." in t:
        t = t.replace(",", "")
    # If only comma exists, treat as decimal separator.
    elif "," in t and "." not in t:
        t = t.replace(",", ".")
    try:
        return float(t)
    except Exception:
        return None


async def _fetch_and_parse(url: str) -> dict[str, Any]:
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0, connect=10.0), follow_redirects=True) as client:
        resp = await client.get(url, headers={"User-Agent": "WatNu18-school-project/1.0"})
        resp.raise_for_status()
        html = resp.text

    soup = BeautifulSoup(html, "lxml")

    # DUO pages have lots of layout; we focus on headings and tables under them.
    # We'll extract for MBO and (optionally) HBO/University if present.
    text_blob = soup.get_text("\n", strip=True)

    last_changed = None
    m = re.search(r"Last changes made on\s+(\d{1,2}\s+\w+\s+\d{4})", text_blob)
    if m:
        last_changed = m.group(1)
    # Dutch variant sometimes: "Laatst gewijzigd op"
    m2 = re.search(r"Laatst gewijzigd op\s+(\d{1,2}\s+\w+\s+\d{4})", text_blob)
    if m2:
        last_changed = m2.group(1)

    def extract_section_tables(section_title_contains: str) -> list[dict[str, Any]]:
        # Find a heading whose text contains phrase, then take following tables until next heading.
        tables: list[dict[str, Any]] = []
        headings = soup.find_all(["h2", "h3"])
        for h in headings:
            title = h.get_text(" ", strip=True).lower()
            if section_title_contains.lower() not in title:
                continue

            # Walk forward in document order (not just siblings), collecting tables until next heading.
            for el in h.find_all_next():
                if getattr(el, "name", None) in ["h2", "h3"]:
                    break
                if getattr(el, "name", None) == "table":
                    tables.append(_table_to_json(el))
            break
        return tables

    mbo_tables = extract_section_tables("mbo")
    hbo_tables = extract_section_tables("university")
    if not hbo_tables:
        # sometimes heading is "HBO and university" or Dutch "hbo en universiteit"
        hbo_tables = extract_section_tables("hbo")

    return {
        "source": {"name": "DUO", "url": url, "last_changed": last_changed},
        "mbo": mbo_tables,
        "hbo_university": hbo_tables,
    }


def _table_to_json(table) -> dict[str, Any]:
    # Convert an HTML table to a simple structure:
    # headers = ["Living with parents", "Living away from home"]
    # rows = [{"label":"Basic grant","values":["€107.26","€350.03"], "values_eur":[107.26,350.03]}, ...]
    headers: list[str] = []
    thead = table.find("thead")
    if thead:
        ths = thead.find_all("th")
        headers = [th.get_text(" ", strip=True) for th in ths]
    else:
        # Some pages have first row as headers
        first_tr = table.find("tr")
        if first_tr:
            ths = first_tr.find_all(["th", "td"])
            headers = [th.get_text(" ", strip=True) for th in ths]

    tbody = table.find("tbody") or table
    rows_out: list[dict[str, Any]] = []
    for tr in tbody.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue
        label = cells[0].get_text(" ", strip=True)
        values = [c.get_text(" ", strip=True) for c in cells[1:]]
        rows_out.append(
            {
                "label": label,
                "values": values,
                "values_eur": [_parse_money(v) for v in values],
            }
        )

    return {"headers": headers, "rows": rows_out}

