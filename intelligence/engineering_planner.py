import json
import ollama

from core.config import MODEL


SYSTEM_PROMPT = """
You are Jarvis, an autonomous software engineer.

Your job is to create an engineering plan.

Return ONLY valid JSON.

Each step must contain an action and any required arguments.

Allowed actions:

project_search
read_code
analyze_code
write_code
generate_patch
apply_patch
run_python
run_terminal
debug
test

Never explain.
Never use markdown.
Return only a JSON array.
"""


class EngineeringPlanner:

    def _build_prompt(self, request):

        if isinstance(request, str):
            return request

        if not isinstance(request, dict):
            return str(request)

        goal = request.get("goal", "")

        files = request.get("project_files", [])

        total = request.get("total_files", len(files))

        preview = "\n".join(files[:50])

        return f"""
Goal:
{goal}

Project contains {total} Python files.

Files:

{preview}

Create the smallest engineering plan needed to solve the goal.

Return ONLY JSON.
"""

    def plan(self, request):

        prompt = self._build_prompt(request)

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response["message"]["content"].strip()

        if text.startswith("```json"):
            text = text[7:]

        elif text.startswith("```"):
            text = text[3:]

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        try:
            return json.loads(text)

        except Exception:
            return [
                {
                    "action": "error",
                    "reason": text
                }
            ]


engineering_planner = EngineeringPlanner()