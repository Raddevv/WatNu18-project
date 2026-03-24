from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path


def _normalize_question(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def _make_id(normalized_question: str) -> str:
    # stable-ish, short, readable id without storing any user identifiers
    # (not cryptographically secure; good enough for a school project)
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
            )
        return items

    def _write(self, items: dict[str, TopQItem]) -> None:
        raw = {
            _id: {
                "question": v.question,
                "answer": v.answer,
                "count": v.count,
                "updated_at": v.updated_at,
            }
            for _id, v in items.items()
        }
        tmp_path = self.path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp_path, self.path)

    def upsert_and_increment(self, question: str, answer: str) -> TopQItem:
        normalized = _normalize_question(question)
        _id = _make_id(normalized)
        now = int(time.time())
        items = self._read()
        if _id in items:
            existing = items[_id]
            existing.count += 1
            existing.updated_at = now
            if not existing.answer:
                existing.answer = answer
            items[_id] = existing
        else:
            items[_id] = TopQItem(
                id=_id,
                question=question.strip(),
                answer=answer.strip(),
                count=1,
                updated_at=now,
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

