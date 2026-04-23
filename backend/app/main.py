from __future__ import annotations

import os
import pathlib
import sys
from typing import AsyncIterator

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from .llm import LLMError, stream_chat_completion
from .models import ChatRequest, TopQuestionsResponse
from .sources.duo_amounts import DuoAmountsClient
from .storage import TopQuestionsStore


load_dotenv()

APP_ENV = os.getenv("APP_ENV", "dev")
FAQ_STORE_PATH = os.getenv("FAQ_STORE_PATH", "./data/top_questions.json")


app = FastAPI(title="WatNu18 Chatbot API")

if APP_ENV == "dev":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://localhost:51730",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:51730",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

store = TopQuestionsStore(FAQ_STORE_PATH)
duo_amounts = DuoAmountsClient()

@app.get("/api/health")
def health() -> dict:
    return {"ok": True}


def _default_system_prompt(locale: str | None) -> str:
    if (locale or "").lower().startswith("nl"):
        return (
            "Je bent de behulpzame chatbot van WatNu18 genaamd Noa, een site voor MBO-studenten die 18 worden. "
            "Antwoord kort, duidelijk en praktisch in het Nederlands. "
            "Als iets afhangt van persoonlijke situatie of de regels kunnen wijzigen, zeg dat erbij en verwijs naar DUO/overheid. "
            "Vraag 1 verduidelijkende vraag als dat nodig is. "
            "Je mag **bold** en *italic* text gebruiken. "
            "Voeg altijd aan het einde van je antwoord 'Sources: ...' toe met de bronnen die je hebt gebruikt."
        )
    return (
        "You are the helpful WatNu18 chatbot named Noa. Answer clearly and practically in Dutch. "
        "If rules can change or depend on the user's situation, say so and suggest official sources. "
        "Always ask for someone's age to give correct information. "
        "Try to implement direct actions where relevant (e.g. 'You can apply for this grant on the DUO website: https://www.duo.nl/particulier/studiefinanciering-aanvragen/aanvragen.jsp'). "
        "If someone asks for amounts, provide the latest official DUO amounts (if relevant; cite DUO as source). "
        "Always answer in Dutch, even if the question is in English or another language. "
        "You can use **bold** and *italic* text. "
        "Always end your response with 'Sources: ...' listing the sources you used."
    )


@app.post("/api/chat")
async def chat(req: ChatRequest):
    messages = list(req.messages)
    if not messages or messages[0].role != "system":
        from .models import ChatMessage

        messages = [ChatMessage(role="system", content=_default_system_prompt(req.locale))] + messages

    user_question = next((m.content for m in reversed(messages) if m.role == "user"), "").strip()
    if not user_question:
        raise HTTPException(status_code=400, detail="Missing user question.")

    ql = user_question.lower()
    amount_keywords = [
        "bedrag",
        "bedragen",
        "amount",
        "amounts",
        "basisbeurs",
        "aanvullende",
        "aanvullende beurs",
        "student finance",
        "studiefinanciering",
        "mbo",
        "uitwonend",
        "thuiswonend",
    ]
    if any(k in ql for k in amount_keywords):
        try:
            facts = await duo_amounts.get_amounts(locale=req.locale)
            from .models import ChatMessage

            facts_msg = (
                "Official DUO amounts snapshot (use these numbers if relevant; cite DUO as source):\n"
                f"Source: {facts.get('source', {}).get('url')}\n"
                f"Last changed: {facts.get('source', {}).get('last_changed')}\n"
                f"MBO tables: {facts.get('mbo')}\n"
            )
            messages = [ChatMessage(role="system", content=facts_msg)] + messages
        except Exception:
            # als DUO tijdelijk niet bereikbaar is, willen we de hele chatbot niet laten falen. We loggen de fout en gaan door zonder de feiten toe te voegen.
            logging.error("DUO FAIL.", exc_info=True)
            pass

    async def sse() -> AsyncIterator[bytes]:
        assistant_text_parts: list[str] = []
        try:
            async for token in stream_chat_completion(messages):
                assistant_text_parts.append(token)
                yield f"data: {token}\n\n".encode("utf-8")
        except LLMError as e:
            yield f"event: error\ndata: {str(e)}\n\n".encode("utf-8")
            return
        except Exception:
            yield "event: error\ndata: Unexpected server error.\n\n".encode("utf-8")
            return

        assistant_text = "".join(assistant_text_parts).strip()
        if req.log_to_faq and assistant_text:
            store.upsert_and_increment(user_question, assistant_text)
            yield "event: logged\ndata: ok\n\n".encode("utf-8")

        yield "event: done\ndata: ok\n\n".encode("utf-8")

    return StreamingResponse(
        sse(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/sources/duo/amounts")
async def get_duo_amounts(locale: str | None = "nl-NL", force_refresh: bool = False):
    """
    Structured amounts from DUO (cached).
    """
    return await duo_amounts.get_amounts(locale=locale, force_refresh=force_refresh)


@app.get("/api/top-questions", response_model=TopQuestionsResponse)
def top_questions(limit: int = 10):
    items = store.top(limit=limit)
    return {
        "items": [
            {"id": i.id, "question": i.question, "answer": i.answer, "count": i.count} for i in items
        ]
    }


@app.get("/api/top-questions/{item_id}")
def get_top_question(item_id: str):
    item = store.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found.")
    return {"id": item.id, "question": item.question, "answer": item.answer, "count": item.count}