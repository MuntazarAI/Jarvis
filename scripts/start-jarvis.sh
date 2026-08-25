#!/usr/bin/env bash
# scripts/start-jarvis.sh — simple helper to activate venv and run the project entrypoint
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."
cd "$ROOT_DIR"

# Activate venv if present
if [ -f "$ROOT_DIR/.venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "$ROOT_DIR/.venv/bin/activate"
fi

# Prefer main.py, fall back to jarvis.py
if [ -f "$ROOT_DIR/main.py" ]; then
  python "$ROOT_DIR/main.py" "$@"
elif [ -f "$ROOT_DIR/jarvis.py" ]; then
  python "$ROOT_DIR/jarvis.py" "$@"
else
  echo "No entrypoint found (main.py or jarvis.py). Run the desired script manually."
  exit 1
fi