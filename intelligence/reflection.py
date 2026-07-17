import json
import ollama

from core.config import MODEL


class Reflection:

    def reply(self, user_message, tool_result):
        """
        Turn tool output into a natural answer.
        """

        if isinstance(tool_result, str):
            return tool_result

        prompt = f"""
The user said:

{user_message}

The tool returned:

{tool_result}

Your job:

- NEVER explain what the tool did.
- NEVER say "according to the tool".
- NEVER say "the tool returned".
- NEVER mention JSON.
- NEVER mention execution.

Simply answer the user's question naturally.

Examples:

User: List files
Answer:
README.md
main.py
core/
brain/

User: Search memory for Rust
Answer:
I found:

profile.favorite_language = Rust

User: Who are you?
Answer:
I'm Jarvis, your AI assistant.

Keep answers short.
"""

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()


reflection = Reflection()