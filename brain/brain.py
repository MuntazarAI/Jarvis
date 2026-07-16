import ollama

from brain.multiplanner import multiplanner
from brain.system_prompt import SYSTEM_PROMPT
from core.config import MODEL


class Brain:
    """
    Sends the user's request to the LLM and converts the response
    into one or more executable plans.
    """

    def think(self, user_message):

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        text = response["message"]["content"]

        return multiplanner.plan(text)


brain = Brain()