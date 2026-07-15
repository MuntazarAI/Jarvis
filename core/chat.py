import json
import re

from core.llm import ask_llm
from core.memory import remember, search
from core.memory_ai import extract_memory
from core.planner import planner
from core.commands import execute

MAX_HISTORY = 20
history = []


def retrieve_relevant_memory(prompt: str):

    words = re.findall(r"\w+", prompt.lower())

    results = []
    seen = set()

    for word in words:

        if len(word) < 3:
            continue

        for match in search(word):

            key = (match["path"], str(match["value"]))

            if key not in seen:
                seen.add(key)
                results.append(match)

    if not results:
        return "No relevant memories."

    return "\n".join(
        f"{m['path']} = {m['value']}"
        for m in results
    )


def ask(prompt: str):

    # -----------------------------
    # Decide what this request is
    # -----------------------------

    plan = planner.create_plan(prompt)

    # -----------------------------
    # Execute command
    # -----------------------------

    result = execute(plan)

    if result is not None:
        return result

    # -----------------------------
    # Store memories
    # -----------------------------

    remember(extract_memory(prompt))

    # -----------------------------
    # Retrieve relevant memories
    # -----------------------------

    memory_text = retrieve_relevant_memory(prompt)

    history.append(
        {
            "role": "user",
            "content":
                f"Relevant memories:\n\n"
                f"{memory_text}\n\n"
                f"User: {prompt}"
        }
    )

    reply = ask_llm(history)

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    if len(history) > MAX_HISTORY:
        history[:] = history[-MAX_HISTORY:]

    return reply