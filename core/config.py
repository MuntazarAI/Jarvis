import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT_DIR / "config" / "defaults.json"

DEFAULTS = {
    "username": "Muntazar",
    "assistant_name": "Jarvis",
    "log_level": "INFO",
    "data_dir": "data",
    "model": "qwen2.5:3b",
    "max_workers": 4,
    "use_gpu": False,
    "http_port": 8080,
    "plugins": [],
}

config = DEFAULTS.copy()

if CONFIG_PATH.exists():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config.update(json.load(f))
    except Exception:
        pass

USERNAME = os.getenv("USERNAME", config.get("username", DEFAULTS["username"]))
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", config.get("assistant_name", DEFAULTS["assistant_name"]))

MODEL = os.getenv("MODEL", config.get("model", DEFAULTS["model"])) or "qwen2.5:3b"

if MODEL == "local":
    MODEL = "qwen2.5:3b"

# Backward compatibility
OLLAMA_MODEL = MODEL