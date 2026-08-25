from tools.registry import registry


class MultiExecutor:
    """
    Executes one or more tool calls.
    """

    def execute(self, plans):

        if plans is None:
            return None

        # ------------------------------
        # Always work with a list
        # ------------------------------

        if not isinstance(plans, list):
            plans = [plans]

        results = []

        for plan in plans:

            tool_name = plan.get("tool")

            # Normal conversation
            if tool_name is None:

                results.append(
                    plan.get("response", plan)
                )
                continue

            tool = registry.get(tool_name)

            if tool is None:

                results.append({
                    "tool": tool_name,
                    "success": False,
                    "error": f"Tool '{tool_name}' not found."
                })

                continue

            arguments = plan.get("arguments", {})

            result = tool.execute(arguments)

            results.append({
                "tool": tool_name,
                "result": result
            })

        # If there was only one step,
        # return only that result.
        if len(results) == 1:

            item = results[0]

            if isinstance(item, dict) and "result" in item:
                return item["result"]

            return item

        return results


multiexecutor = MultiExecutor()