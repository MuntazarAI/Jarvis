import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "Muntazar")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")

# Ollama model
MODEL = "qwen2.5:3b"

# Backward compatibility
OLLAMA_MODEL = MODEL