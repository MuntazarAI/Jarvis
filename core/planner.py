"""
planner.py

Jarvis decision engine.

The planner decides what kind of request the user is making before the
assistant chooses how to respond.

Example:

User: Open Firefox
-> intent = system

User: Remember my birthday
-> intent = memory

User: Search Python decorators
-> intent = browser

User: What is quantum computing?
-> intent = chat
"""

from dataclasses import dataclass
import re


@dataclass
class Plan:
    intent: str
    action: str
    target: str


class Planner:

    def __init__(self):

        self.browser_words = {
            "search",
            "google",
            "bing",
            "find",
            "lookup",
        }

        self.memory_words = {
            "remember",
            "forget",
            "recall",
        }

        self.system_words = {
            "open",
            "close",
            "launch",
            "start",
            "shutdown",
            "restart",
        }

    def create_plan(self, prompt: str) -> Plan:

        text = prompt.lower().strip()

        words = set(re.findall(r"\w+", text))

        # --------------------------
        # MEMORY
        # --------------------------

        if words & self.memory_words:

            if "forget" in words:
                return Plan(
                    intent="memory",
                    action="forget",
                    target=text,
                )

            return Plan(
                intent="memory",
                action="remember",
                target=text,
            )

        # --------------------------
        # BROWSER
        # --------------------------

        if words & self.browser_words:

            query = text

            if query.startswith("search "):
                query = query[7:].strip()

            return Plan(
                intent="browser",
                action="search",
                target=query,
            )

        # --------------------------
        # SYSTEM
        # --------------------------

        if words & self.system_words:

            first = text.split()

            target = ""

            if len(first) > 1:
                target = " ".join(first[1:])

            return Plan(
                intent="system",
                action="run",
                target=target,
            )

        # --------------------------
        # DEFAULT
        # --------------------------

        return Plan(
            intent="chat",
            action="answer",
            target=text,
        )


planner = Planner()
