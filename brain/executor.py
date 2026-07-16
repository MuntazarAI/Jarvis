import json

import tools
from tools.registry import registry


class Executor:

    def execute(self, plan):

        if isinstance(plan, str):

            try:
                plan = json.loads(plan)

            except Exception:
                return plan

        if not isinstance(plan, dict):
            return plan

        tool_name = plan.get("tool")

        if tool_name is None:
            return plan.get("response", plan)

        tool = registry.get(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' not found."

        arguments = plan.get("arguments", {})

        try:
            return tool.execute(arguments)

        except Exception as e:
            return {
                "error": str(e)
            }


executor = Executor()