import ollama

from core.config import MODEL
from runtime.read_code import read_code


SYSTEM_PROMPT = """
You are an expert Python software engineer.

Rewrite the ENTIRE Python file to satisfy the goal.

Rules:
- Output ONLY valid Python source code.
- Do NOT use markdown.
- Do NOT use triple backticks.
- Do NOT explain anything.
- Preserve working code whenever possible.
"""


class PatchGenerator:
    """
    Generates a complete replacement for a source file.
    """

    def generate(self, path: str, goal: str):

        source = read_code.read(path)

        if not source.get("success", False):
            return source

        prompt = f"""
Goal:

{goal}

File:

{path}

Source Code:

{source["content"]}
"""

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        patched = response["message"]["content"].strip()

        if patched.startswith("```python"):
            patched = patched[9:]

        elif patched.startswith("```"):
            patched = patched[3:]

        if patched.endswith("```"):
            patched = patched[:-3]

        patched = patched.strip()

        return {
            "success": True,
            "path": path,
            "original": source["content"],
            "patched": patched,
        }


patch_generator = PatchGenerator()

# Backward compatibility
generate_patch = patch_generator
