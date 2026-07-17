import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "Muntazar")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")

# Ollama model
MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:14b")

# Backward compatibility
OLLAMA_MODEL = MODEL