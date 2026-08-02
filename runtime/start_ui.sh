#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if [ ! -d .venv ]; then
  echo "Creating virtual environment .venv"
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt -r runtime/requirements-ui.txt

PORT=${PORT:-8080}
for candidate in "$PORT" 8081 8082 8083; do
  if ! ss -ltn "sport = :$candidate" | grep -q LISTEN; then
    PORT=$candidate
    break
  fi
  echo "Port $candidate is in use. Trying next port..."
done

echo "Starting server on port $PORT"
PORT=$PORT python runtime/server.py
