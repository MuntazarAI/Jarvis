import re

from core.llm import ask_llm
from core.memory import remember, search
from core.memory_ai import extract_memory

MAX_HISTORY = 20

history = []


def retrieve_relevant_memory(prompt: str) -> str:
    """
    Retrieve only the memories related to the user's question.
    """

    words = re.findall(r"[a-zA-Z0-9_]+", prompt.lower())

    seen = set()
    results = []

    for word in words:

        if len(word) < 3:
            continue

        for item in search(word):

            key = (item["path"], str(item["value"]))

            if key not in seen:
                seen.add(key)
                results.append(item)

    if not results:
        return ""

    text = []

    for item in results:
        text.append(f"{item['path']}: {item['value']}")

    return "\n".join(text)


def ask(prompt: str) -> str:

    # Save any new memories
    new_memory = extract_memory(prompt)

    if new_memory:
        remember(new_memory)

    # Retrieve relevant memories
    relevant = retrieve_relevant_memory(prompt)

    if relevant:

        system_prompt = f"""
You are Jarvis.

These are facts stored in long-term memory.

{relevant}

Use these facts when answering.
If the answer is present here, NEVER say you don't know.
"""

    else:

        system_prompt = """
You are Jarvis.
Answer normally.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    print("\n======================")
    print("SYSTEM PROMPT")
    print("======================")
    print(system_prompt)
    print("======================\n")

    reply = ask_llm(messages)

    history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )

    if len(history) > MAX_HISTORY:
        history[:] = history[-MAX_HISTORY:]

    return reply
