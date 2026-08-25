#!/usr/bin/env bash
# install.sh — small installer to set up a Python virtualenv and install requirements
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

# Create virtualenv if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment in .venv..."
  python3 -m venv .venv
fi

# Activate
# shellcheck disable=SC1091
source .venv/bin/activate

# Upgrade pip and install requirements if present
if [ -f requirements.txt ]; then
  echo "Installing Python requirements..."
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "No requirements.txt found — skipping pip install"
fi

echo "Setup complete. Activate with: source .venv/bin/activate"