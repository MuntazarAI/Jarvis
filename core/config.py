import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "Muntazar")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
