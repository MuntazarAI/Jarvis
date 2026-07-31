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
python runtime/server.py
