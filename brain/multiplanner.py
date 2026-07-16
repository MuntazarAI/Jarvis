import json


class MultiPlanner:
    """
    Parses single-step and multi-step plans returned by the LLM.
    """

    def plan(self, response):

        # Already parsed
        if isinstance(response, dict):

            if "steps" in response:
                return response["steps"]

            return [response]

        # Try parsing JSON
        try:
            plan = json.loads(response)

            if isinstance(plan, dict):

                if "steps" in plan:
                    return plan["steps"]

                return [plan]

            if isinstance(plan, list):
                return plan

        except Exception:
            pass

        # Normal conversation
        return [
            {
                "tool": None,
                "response": response
            }
        ]


multiplanner = MultiPlanner()