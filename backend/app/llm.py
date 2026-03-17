from __future__ import annotations

import os
from typing import AsyncIterator

import httpx

from .models import ChatMessage


class LLMError(RuntimeError):
    pass


def _env(name: str, default: str | None = None) -> str | None:
    v = os.getenv(name)
    if v is None or v.strip() == "":
        return default
    return v


async def stream_chat_completion(messages: list[ChatMessage]) -> AsyncIterator[str]:
    provider = (_env("LLM_PROVIDER", "openai") or "openai").lower()
    if provider == "ollama":
        async for chunk in _ollama_stream(messages):
            yield chunk
        return

    # default: openai-compatible (OpenAI API)
    async for chunk in _openai_stream(messages):
        yield chunk


async def _openai_stream(messages: list[ChatMessage]) -> AsyncIterator[str]:
    api_key = _env("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("Missing OPENAI_API_KEY. Set it in backend/.env (copy from .env.example).")

    model = _env("OPENAI_MODEL", "gpt-4.1-mini") or "gpt-4.1-mini"
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": model,
        "messages": [m.model_dump() for m in messages],
        "stream": True,
        "temperature": 0.2,
    }

    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0, connect=10.0)) as client:
        async with client.stream(
            "POST",
            url,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
        ) as resp:
            if resp.status_code >= 400:
                body = await resp.aread()
                raise LLMError(f"OpenAI error {resp.status_code}: {body[:500].decode('utf-8', 'ignore')}")

            async for line in resp.aiter_lines():
                if not line or not line.startswith("data:"):
                    continue
                data = line.removeprefix("data:").strip()
                if data == "[DONE]":
                    break
                try:
                    event = httpx.Response(200, content=data).json()
                    delta = event["choices"][0]["delta"]
                    token = delta.get("content")
                    if token:
                        yield token
                except Exception:
                    continue


async def _ollama_stream(messages: list[ChatMessage]) -> AsyncIterator[str]:
    base_url = _env("OLLAMA_BASE_URL", "http://localhost:11434") or "http://localhost:11434"
    model = _env("OLLAMA_MODEL", "llama3.1:8b") or "llama3.1:8b"
    url = f"{base_url.rstrip('/')}/api/chat"

    payload = {
        "model": model,
        "messages": [m.model_dump() for m in messages if m.role != "system"],
        "stream": True,
        "options": {"temperature": 0.2},
    }

    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0, connect=10.0)) as client:
        async with client.stream("POST", url, json=payload) as resp:
            if resp.status_code >= 400:
                body = await resp.aread()
                raise LLMError(f"Ollama error {resp.status_code}: {body[:500].decode('utf-8', 'ignore')}")

            async for line in resp.aiter_lines():
                if not line:
                    continue
                try:
                    event = httpx.Response(200, content=line).json()
                    if event.get("done"):
                        break
                    msg = event.get("message") or {}
                    token = msg.get("content")
                    if token:
                        yield token
                except Exception:
                    continue

