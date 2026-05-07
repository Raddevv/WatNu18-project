from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


def _normalize_question(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text)
    return text


def _stem_tokens(tokens: Iterable[str]) -> list[str]:
    stems: list[str] = []
    for token in tokens:
        t = token
        for suffix in ("eren", "en", "tje", "jes", "s"):
            if len(t) > 4 and t.endswith(suffix):
                t = t[: -len(suffix)]
                break
        stems.append(t)
    return stems


def _question_tokens(text: str) -> set[str]:
    stopwords = {
        "de", "het", "een", "en", "of", "ik", "je", "jij", "wij", "wat", "hoe", "kan", "kun",
        "mijn", "voor", "met", "als", "bij", "op", "in", "te", "van", "is", "zijn",
    }
    normalized = _normalize_question(text)
    tokens = [t for t in normalized.split(" ") if len(t) > 2 and t not in stopwords]
    return set(_stem_tokens(tokens))


def _similarity(a: str, b: str) -> float:
    ta = _question_tokens(a)
    tb = _question_tokens(b)
    if not ta or not tb:
        return 0.0
    intersection = len(ta.intersection(tb))
    union = len(ta.union(tb))
    jaccard = intersection / union if union else 0.0
    containment = intersection / min(len(ta), len(tb))
    return max(jaccard, containment * 0.85)


def _make_id(normalized_question: str) -> str:
    import hashlib

    h = hashlib.sha256(normalized_question.encode("utf-8")).hexdigest()
    return h[:12]


@dataclass
class TopQItem:
    id: str
    question: str
    answer: str
    count: int
    updated_at: int
    aliases: dict[str, int]
    merge_events: list[dict[str, str | float | int]]


class TopQuestionsStore:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read(self) -> dict[str, TopQItem]:
        if not self.path.exists():
            return {}
        raw = json.loads(self.path.read_text(encoding="utf-8") or "{}")
        items: dict[str, TopQItem] = {}
        for _id, v in raw.items():
            items[_id] = TopQItem(
                id=_id,
                question=v["question"],
                answer=v["answer"],
                count=int(v.get("count", 0)),
                updated_at=int(v.get("updated_at", 0)),
                aliases=dict(v.get("aliases", {})),
                merge_events=list(v.get("merge_events", [])),
            )
        return items

    def _write(self, items: dict[str, TopQItem]) -> None:
        raw = {
            _id: {
                "question": v.question,
                "answer": v.answer,
                "count": v.count,
                "updated_at": v.updated_at,
                "aliases": v.aliases,
                "merge_events": v.merge_events,
            }
            for _id, v in items.items()
        }
        tmp_path = self.path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp_path, self.path)

    def _register_alias(self, item: TopQItem, question: str) -> None:
        q = question.strip()
        if not q:
            return
        item.aliases[q] = int(item.aliases.get(q, 0)) + 1

    def _register_merge_event(
        self,
        item: TopQItem,
        incoming_question: str,
        score: float,
        matched_on: str,
        now: int,
    ) -> None:
        item.merge_events.append(
            {
                "incoming_question": incoming_question.strip(),
                "matched_on": matched_on.strip(),
                "score": round(score, 4),
                "at": now,
            }
        )
        # Keep payload small and useful for debugging.
        item.merge_events = item.merge_events[-20:]

    def upsert_and_increment(self, question: str, answer: str) -> TopQItem:
        normalized = _normalize_question(question)
        _id = _make_id(normalized)
        now = int(time.time())
        items = self._read()
        best_id: str | None = None
        best_score = 0.0
        for item_id, item in items.items():
            score = _similarity(question, item.question)
            if score > best_score:
                best_id = item_id
                best_score = score

        # Merge near-duplicate question intent to keep Top 10 useful.
        merge_threshold = 0.62

        if _id in items:
            existing = items[_id]
            existing.count += 1
            existing.updated_at = now
            self._register_alias(existing, question)
            if not existing.answer:
                existing.answer = answer
            items[_id] = existing
        elif best_id and best_score >= merge_threshold:
            existing = items[best_id]
            existing.count += 1
            existing.updated_at = now
            self._register_alias(existing, question)
            self._register_merge_event(
                existing,
                incoming_question=question,
                score=best_score,
                matched_on=existing.question,
                now=now,
            )
            if not existing.answer:
                existing.answer = answer
            items[best_id] = existing
            _id = best_id
        else:
            items[_id] = TopQItem(
                id=_id,
                question=question.strip(),
                answer=answer.strip(),
                count=1,
                updated_at=now,
                aliases={question.strip(): 1} if question.strip() else {},
                merge_events=[],
            )
        self._write(items)
        return items[_id]

    def top(self, limit: int = 10) -> list[TopQItem]:
        items = list(self._read().values())
        items.sort(key=lambda x: (x.count, x.updated_at), reverse=True)
        return items[:limit]

    def get(self, _id: str) -> TopQItem | None:
        items = self._read()
        return items.get(_id)

    def debug_clusters(self, limit: int = 10) -> list[dict]:
        clusters: list[dict] = []
        for item in self.top(limit=limit):
            aliases_sorted = sorted(item.aliases.items(), key=lambda kv: kv[1], reverse=True)
            clusters.append(
                {
                    "id": item.id,
                    "canonical_question": item.question,
                    "count": item.count,
                    "aliases": [{"question": q, "count": c} for q, c in aliases_sorted],
                    "recent_merges": item.merge_events[-10:],
                }
            )
        return clusters

