# WatNu18 Chatbot backend (FastAPI)

## Run locally (Windows)

From the repo root:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
copy .env.example .env
```

Fill in **one** of:

- `OPENAI_API_KEY=...` (recommended easiest)
- or set `LLM_PROVIDER=ollama` and run Ollama locally

Start the API:

```powershell
.\.venv\Scripts\uvicorn app.main:app --reload --port 8000
```

Health check:

- `GET http://localhost:8000/api/health`

## Frontend dev (Vite)

Your Vite dev server proxies `/api/*` to `http://localhost:8000`, so the Vue app can call the backend without extra CORS config.

