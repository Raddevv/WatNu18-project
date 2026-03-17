#!/bin/bash
set -e

PURPLE='\033[0;35m'
LIGHT_PURPLE='\033[1;35m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

clear
echo -e "${LIGHT_PURPLE}==============================================${NC}"
echo -e "${LIGHT_PURPLE}  Watnu18 — Local Development (frontend + hooks) ${NC}"
echo -e "${LIGHT_PURPLE}==============================================${NC}"
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
echo -e "${LIGHT_PURPLE}>>> Pre-flight checks...${NC}"

command -v docker >/dev/null || { echo -e "${RED}Docker not found${NC}"; exit 1; }
[[ -f docker-compose.yml ]] || { echo -e "${RED}docker-compose.yml missing${NC}"; exit 1; }
[[ -f Dockerfile ]] || { echo -e "${RED}Dockerfile missing${NC}"; exit 1; }

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
  echo -e "${LIGHT_PURPLE}>>> Building Docker images...${NC}"
  docker compose build --no-cache
  touch .docker_built
else
  echo -e "${LIGHT_PURPLE}>>> Using existing Docker images${NC}"
fi

# === BACKEND / LARAVEL SETUP ===
# Laravel setup removed: if you have backend setup steps (composer, artisan, migrations)
# you can add them to a separate `start_backend.sh` and the startup script will
# launch it as a background hook later. Keeping script focused on frontend.

# === FRONTEND / VITE SETUP ===
echo -e "${LIGHT_PURPLE}>>> Checking frontend dependencies (local vite/)...${NC}"
if [[ -d "vite" ]]; then
  if [[ ! -d "vite/node_modules" || ! -f vite/node_modules/.bin/vite ]]; then
    echo -e "${LIGHT_PURPLE}>>> Installing frontend dependencies in vite/...${NC}"
    (cd vite && npm install)
  else
    echo -e "${GREEN}>>> Frontend dependencies OK${NC}"
  fi
else
  echo -e "${RED}>>> Warning: vite/ directory not found — frontend will be skipped${NC}"
fi
touch .frontend_done

# === START SERVICES ===
echo -e "${PURPLE}>>> Starting services...${NC}"

if $WATCH_MODE; then
  echo -e "${LIGHT_PURPLE}>>> Watch mode enabled${NC}"
  docker compose watch
else
  echo -e "${GREEN}>>> Services starting...${NC}"
  echo -e "${PURPLE}Vite (frontend): http://localhost:51730${NC}"
  echo -e "${PURPLE}App (PHP-FPM): http://localhost:9001${NC}"
  echo -e "${PURPLE}Postgres: localhost:54320${NC}"
  echo -e "${PURPLE}Redis: localhost:16379${NC}"
  echo -e "${PURPLE}${NC}"
  echo -e "${LIGHT_PURPLE}>>> Live console output:${NC}"
  echo -e "${PURPLE}(Press Ctrl+C to stop all services)${NC}"
  echo

  # Start all services in background
  docker compose up -d

  # Give containers time to start
  sleep 2

  # Show live logs from all services with colors
  docker compose logs -f
fi