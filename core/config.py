import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "Muntazar")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")
MODEL = "llama3.2:3b"
