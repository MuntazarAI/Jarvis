import json
import ollama

from core.config import MODEL


class PatchGenerator:
    """
    Generates structured code patches using the LLM.

    Output schema:

    {
        "patches": [
            {
                "file": "...",
                "action": "replace",
                "old": "...",
                "new": "..."
            }
        ],
        "reason": "..."
    }
    """

    def generate(
        self,
        source,
        analysis,
        error,
        diagnosis
    ):

        prompt = f"""
You are an elite Python software engineer.

Your job is to repair Python programs.

Return ONLY valid JSON.

Schema:

{{
    "patches": [
        {{
            "file": "...",
            "action": "replace",
            "old": "...",
            "new": "..."
        }}
    ],
    "reason": "..."
}}

SOURCE

{json.dumps(source, indent=4)}

ANALYSIS

{json.dumps(analysis, indent=4)}

ERROR

{json.dumps(error, indent=4)}

DIAGNOSIS

{json.dumps(diagnosis, indent=4)}

Rules:

- Return ONLY JSON.
- Never explain.
- Never use markdown.
- Preserve formatting.
"""

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response["message"]["content"].strip()

        try:
            return json.loads(text)

        except Exception:

            start = text.find("{")
            end = text.rfind("}")

            if start != -1 and end != -1:
                try:
                    return json.loads(text[start:end + 1])
                except Exception:
                    pass

            return {
                "patches": [],
                "reason": text
            }


patch_generator = PatchGenerator()