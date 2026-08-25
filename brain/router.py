import re


class Router:
    """
    Routes obvious requests directly to tools.
    Returns:
        dict -> tool plan
        None -> let the LLM decide
    """

    def route(self, text: str):

        if not text:
            return None

        lower = text.lower().strip()

        # -------------------------
        # MEMORY
        # -------------------------

        if lower in (
            "who am i",
            "who am i?",
            "recall everything",
            "remember everything",
        ):
            return {
                "tool": "memory",
                "arguments": {
                    "action": "recall"
                }
            }

        if lower.startswith("search memory for "):
            keyword = text[len("search memory for "):].strip()

            return {
                "tool": "memory",
                "arguments": {
                    "action": "search",
                    "keyword": keyword
                }
            }

        if lower.startswith("remember "):
            return None

        # -------------------------
        # TERMINAL
        # -------------------------

        if lower == "pwd":
            return {
                "tool": "terminal",
                "arguments": {
                    "command": "pwd"
                }
            }

        if lower == "ls":

            return {
                "tool": "terminal",
                "arguments": {
                    "command": "ls"
                }
            }

        if lower == "list files":

            return {
                "tool": "terminal",
                "arguments": {
                    "command": "ls -l"
                }
            }

        if lower.startswith("run "):

            command = text[4:].strip()

            return {
                "tool": "terminal",
                "arguments": {
                    "command": command
                }
            }

        # -------------------------
        # BROWSER
        # -------------------------

        if lower.startswith("search web for "):

            query = text[len("search web for "):].strip()

            return {
                "tool": "browser",
                "arguments": {
                    "action": "search",
                    "query": query
                }
            }

        # -------------------------
        # Let Brain Decide
        # -------------------------

        return None


router = Router()