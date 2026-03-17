from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1)
    log_to_faq: bool = False
    locale: str | None = "nl-NL"


class TopQuestion(BaseModel):
    id: str
    question: str
    answer: str
    count: int


class TopQuestionsResponse(BaseModel):
    items: list[TopQuestion]
