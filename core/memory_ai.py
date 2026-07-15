import json
from ollama import chat
from core.config import MODEL

SYSTEM_PROMPT = """
You extract long-term facts about the user.

Return ONLY valid JSON.

If nothing should be remembered return:

{}

Example:

{
  "profile": {
    "favorite_color": "Blue",
    "dog_name": "Max",
    "name": "Muntazar",
    "age": 17,
    "location": "India",
    "occupation": "Student"
  },

  "preferences": {
    "favorite_food": "Pizza",
    "favorite_movie": "Interstellar",
    "favorite_music": "Golden Brown"
  },

  "goals": [
    "Build a real JARVIS AI"
  ],

  "projects": [
    {
      "name": "Jarvis",
      "status": "In Development"
    }
  ],

  "notes": [
    "Learning Python"
  ]
}

Never explain.
Never add markdown.
Only return JSON.
"""


def extract_memory(prompt: str) -> dict:
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    text = response["message"]["content"].strip()

    try:
        return json.loads(text)
    except Exception:
        return {}
