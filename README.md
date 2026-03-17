# WatNu18-project

## Quick start (Docker, recommended)

From the repo root:

1) Create your local backend env file:

```powershell
copy backend\.env.example backend\.env
```

2) Start everything:

```powershell
docker compose up -d
```

Frontend: `http://localhost:51730`  
Backend: `http://localhost:8000/api/health`

## Alternative: Bash helper script

If you have Git Bash / WSL:

```bash
cp backend/.env.example backend/.env
./start_frontend.sh
```