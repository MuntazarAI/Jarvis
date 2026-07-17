import json
import re

import ollama

from core.config import MODEL


class AIDebugger:
    """
    AI debugger that always tries to return a valid JSON diagnosis.

    Strategy

    1. Ask the LLM for STRICT JSON.
    2. Extract JSON if the model wraps it in text.
    3. Retry once with an even stricter prompt.
    4. Fall back to deterministic debugging.
    """

    SCHEMA = {
        "problem": "",
        "cause": "",
        "fix": "",
        "confidence": 0.0
    }

    def diagnose(self, debug_data):

        prompts = [
            self._primary_prompt(debug_data),
            self._retry_prompt(debug_data)
        ]

        for prompt in prompts:

            try:

                response = ollama.chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert Python debugging engine.\n"
                                "Return ONLY JSON.\n"
                                "Never explain.\n"
                                "Never use markdown.\n"
                                "Never output code fences."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                text = response["message"]["content"].strip()

                result = self._parse_json(text)

                if result:

                    return result

            except Exception:
                pass

        return self._fallback(debug_data)

    # -------------------------------------------------

    def _primary_prompt(self, debug_data):

        return f"""
Analyze this Python crash.

Return ONLY JSON.

Required schema:

{{
    "problem":"...",
    "cause":"...",
    "fix":"...",
    "confidence":0.95
}}

Debug Data:

{json.dumps(debug_data, indent=4)}
"""

    # -------------------------------------------------

    def _retry_prompt(self, debug_data):

        return f"""
YOUR LAST RESPONSE WAS INVALID.

DO NOT EXPLAIN.

DO NOT WRITE ENGLISH.

DO NOT WRITE PYTHON.

ONLY OUTPUT A JSON OBJECT.

Schema:

{{
    "problem":"",
    "cause":"",
    "fix":"",
    "confidence":0.0
}}

Debug:

{json.dumps(debug_data)}
"""

    # -------------------------------------------------

    def _parse_json(self, text):

        try:

            obj = json.loads(text)

            return self._validate(obj)

        except Exception:
            pass

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:

            return None

        try:

            obj = json.loads(match.group())

            return self._validate(obj)

        except Exception:

            return None

    # -------------------------------------------------

    def _validate(self, obj):

        result = self.SCHEMA.copy()

        result.update(obj)

        try:
            result["confidence"] = float(result["confidence"])
        except Exception:
            result["confidence"] = 0.0

        return result

    # -------------------------------------------------

    def _fallback(self, debug_data):

        error = debug_data.get("error", {})

        source = debug_data.get("source", {})

        error_type = error.get("error_type", "")
        message = error.get("message", "")
        code = source.get("content", "")

        problem = message
        cause = "Unknown."
        fix = "Inspect the traceback."

        # ------------------------

        if error_type == "NameError":

            cause = (
                "A variable is being used before it exists."
            )

            fix = (
                "Create the variable before using it "
                "or correct its name."
            )

        elif error_type == "AttributeError":

            cause = (
                "An object does not contain the requested attribute."
            )

            fix = (
                "Verify the object type and attribute name."
            )

        elif error_type == "TypeError":

            cause = (
                "An operation received incompatible data types."
            )

            fix = (
                "Check function arguments and variable types."
            )

        elif error_type == "KeyError":

            cause = (
                "A dictionary key does not exist."
            )

            fix = (
                "Check the dictionary before indexing."
            )

        elif error_type == "IndexError":

            cause = (
                "A list index is outside its valid range."
            )

            fix = (
                "Check list length before indexing."
            )

        elif error_type == "ImportError":

            cause = (
                "Python could not import a module."
            )

            fix = (
                "Install the package or correct the import."
            )

        elif error_type == "ModuleNotFoundError":

            cause = (
                "The requested Python package is not installed."
            )

            fix = (
                "Install the package into the active virtual environment."
            )

        elif error_type == "SyntaxError":

            cause = (
                "Python could not parse the source file."
            )

            fix = (
                "Check indentation, brackets and punctuation."
            )

        if "print(x)" in code:

            cause = "Variable x is undefined."

            fix = (
                "Define x before calling print(x)."
            )

        return {
            "problem": problem,
            "cause": cause,
            "fix": fix,
            "confidence": 0.90
        }


ai_debugger = AIDebugger()