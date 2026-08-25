import json


class Planner:
    """
    Converts the LLM response into an action plan.
    """

    def plan(self, response: str):

        if not isinstance(response, str):
            return response

        response = response.strip()

        # Remove markdown code fences
        if response.startswith("```json"):
            response = response[7:]

        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        try:
            return json.loads(response)

        except Exception:
            return {
                "tool": None,
                "response": response
            }


planner = Planner()