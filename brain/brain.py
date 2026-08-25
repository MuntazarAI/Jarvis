from brain.multiplanner import multiplanner
from brain.system_prompt import SYSTEM_PROMPT
from core.llm import ask_llm


class Brain:
    """
    Sends the user's request to the LLM and converts the response
    into one or more executable plans.
    """

    def think(self, user_message):

        response_text = ask_llm([
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ])

        text = response_text.strip()

        return multiplanner.plan(text)


brain = Brain()