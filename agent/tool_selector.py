from agent import state


class ToolSelector:
    """
    Decides what should happen after every tool execution.
    """

    def after_action(self, state, result):

        action = state.last_action

        #
        # Special handling for run_python.
        #
        if action == "run_python":
            execution = result.get("data", {})

            if execution.get("success", False):
                
                remaining = state.variables.get("remaining_files", [])

                if remaining:
                    return "continue"

                return "finish"

            return "continue"

        #
        # Runtime tool failed.
        #
        if not result.get("success", False):
            return "abort"

        return "continue"


tool_selector = ToolSelector()