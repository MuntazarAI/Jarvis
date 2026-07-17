import json

from runtime.router import runtime_router


class Executor:
    """
    Executes engineering plans by dispatching every
    action to the Runtime Router.
    """

    def __init__(self):
        self.history = []

    def execute(self, plan):

        if isinstance(plan, str):

            try:
                plan = json.loads(plan)

            except Exception:

                return plan

        #
        # Single action
        #

        if isinstance(plan, dict):

            plan = [plan]

        if not isinstance(plan, list):

            return {
                "success": False,
                "error": "Plan must be a list."
            }

        self.history = []

        for index, step in enumerate(plan, start=1):

            action = step.get("action", "unknown")

            print(f"[{index}/{len(plan)}] {action}")

            result = runtime_router.execute(step)

            self.history.append({
                "step": index,
                "action": action,
                "result": result,
                "success": (
                    result.get("success", True)
                    if isinstance(result, dict)
                    else True
                )
            })

        return self.history


executor = Executor()