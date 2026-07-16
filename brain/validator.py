class Validator:
    """
    Validates plans before they reach the executor.
    """

    def validate(self, plan):

        if not isinstance(plan, dict):
            return True, ""

        tool = plan.get("tool")

        # Normal conversation
        if tool is None:
            return True, ""

        arguments = plan.get("arguments", {})

        # -----------------------------
        # Memory Tool
        # -----------------------------

        if tool == "memory":

            action = arguments.get("action")

            if not action:
                return False, "Memory tool requires an 'action'."

            if action == "search" and not arguments.get("keyword"):
                return False, "Memory search requires a 'keyword'."

            if action == "remember" and not arguments.get("memory"):
                return False, "Memory remember requires 'memory'."

            if action == "forget":
                if not arguments.get("category"):
                    return False, "Memory forget requires 'category'."

                if not arguments.get("key"):
                    return False, "Memory forget requires 'key'."

        # -----------------------------
        # Terminal Tool
        # -----------------------------

        elif tool == "terminal":

            if not arguments.get("command"):
                return False, "Terminal tool requires 'command'."

        # -----------------------------
        # Filesystem Tool
        # -----------------------------

        elif tool == "filesystem":

            if not arguments.get("action"):
                return False, "Filesystem tool requires 'action'."

        # -----------------------------
        # Python Tool
        # -----------------------------

        elif tool == "python":

            if not arguments.get("code"):
                return False, "Python tool requires 'code'."

        # -----------------------------
        # Browser Tool
        # -----------------------------

        elif tool == "browser":

            action = arguments.get("action")

            if not action:
                return False, "Browser tool requires 'action'."

            if action == "search" and not arguments.get("query"):
                return False, "Browser search requires 'query'."

            if action == "open" and not arguments.get("url"):
                return False, "Browser open requires 'url'."

        else:
            return False, f"Unknown tool '{tool}'."

        return True, ""


validator = Validator()
