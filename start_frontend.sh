#!/bin/bash
set -e

CYAN='\033[0;36m'
LIGHT_CYAN='\033[1;36m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

clear
echo -e "${LIGHT_CYAN}==============================================${NC}"
echo -e "${LIGHT_CYAN}  Watnu18 — Local Development (frontend + hooks) ${NC}"
echo -e "${LIGHT_CYAN}  Script by alexljn ${NC}"
echo -e "${LIGHT_CYAN}==============================================${NC}"
echo

# === ARGUMENTS ===
WATCH_MODE=false
FORCE=false
for arg in "$@"; do
  case "$arg" in
    --watch) WATCH_MODE=true ;;
    --force|-f) FORCE=true ;;
  esac
done

# === PREFLIGHT CHECKS ===
echo -e "${LIGHT_CYAN}>>> Pre-flight checks...${NC}"

command -v docker >/dev/null || { echo -e "${RED}Docker not found${NC}"; exit 1; }
[[ -f docker-compose.yml ]] || { echo -e "${RED}docker-compose.yml missing${NC}"; exit 1; }
[[ -f Dockerfile ]] || { echo -e "${RED}Dockerfile missing${NC}"; exit 1; }
[[ -f backend/.env ]] || { echo -e "${RED}backend/.env missing. Create it from backend/.env.example${NC}"; exit 1; }

echo -e "${GREEN}>>> Pre-flight OK${NC}"

# === FORCE CLEAN ===
if $FORCE; then
  echo -e "${RED}>>> FORCE: cleaning old builds, containers, and frontend deps${NC}"
  docker compose down -v --remove-orphans || true
  rm -f .docker_built .laravel_done .frontend_done
  rm -rf vite/node_modules
fi

# === BUILD CONTAINERS ===
if [[ ! -f .docker_built ]]; then
  echo -e "${LIGHT_CYAN}>>> Building Docker images...${NC}"
  docker compose build --no-cache
  touch .docker_built
else
  echo -e "${LIGHT_CYAN}>>> Using existing Docker images${NC}"
fi

# === FRONTEND / VITE SETUP ===
echo -e "${LIGHT_CYAN}>>> Checking frontend dependencies (local vite/)...${NC}"
if [[ -d "vite" ]]; then
  if [[ ! -d "vite/node_modules" || ! -f vite/node_modules/.bin/vite ]]; then
    echo -e "${LIGHT_CYAN}>>> Installing frontend dependencies in vite/...${NC}"
    (cd vite && npm install)
  else
    echo -e "${GREEN}>>> Frontend dependencies OK${NC}"
  fi
else
  echo -e "${RED}>>> Warning: vite/ directory not found — frontend will be skipped${NC}"
fi
touch .frontend_done

# === START SERVICES ===
echo -e "${CYAN}>>> Starting services...${NC}"

if $WATCH_MODE; then
  echo -e "${LIGHT_CYAN}>>> Watch mode enabled${NC}"
  docker compose watch
else
  echo -e "${GREEN}>>> Services starting...${NC}"
  echo -e "${CYAN}Vite (frontend): http://localhost:51730${NC}"
  echo -e "${CYAN}Chatbot API (FastAPI): http://localhost:8000${NC}"
  echo -e "${CYAN}App (PHP-FPM): http://localhost:9001${NC}"
  echo -e "${CYAN}Postgres: localhost:54320${NC}"
  echo -e "${CYAN}Redis: localhost:16379${NC}"
  echo -e "${CYAN}${NC}"
  echo -e "${LIGHT_CYAN}>>> Live console output:${NC}"
  echo -e "${CYAN}(Press Ctrl+C to stop all services)${NC}"
  echo

  # Start all services in background
  docker compose up -d

  # Give containers time to start
  sleep 2

  # Show live logs from all services with colors
  docker compose logs -f
fi