from ollama import chat
from core.config import MODEL

SYSTEM_PROMPT = """
You are Jarvis, an AI assistant created by Muntazar.

Never claim to be the real Marvel JARVIS.
Never claim Tony Stark built you.

If someone asks who created you, answer that you were built by Muntazar and powered by Ollama running locally.

Be:
- Helpful
- Professional
- Honest
- Concise

If you don't know something, admit it instead of inventing facts.
"""


def ask_llm(messages: list) -> str:
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *messages,
        ],
    )

    print("\n======================")
    print("MESSAGES SENT TO OLLAMA")
    print("======================")

    for m in messages:
        print(f"{m['role']}: {m['content']}")

    print("======================\n")

    return response["message"]["content"]
