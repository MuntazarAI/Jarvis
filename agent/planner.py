class AgentPlanner:
    """
    Generates the next actions for the engineering agent.
    """

    def runnable(self, path: str) -> bool:
        """
        Returns True if a Python file should actually be executed.
        """

        # Skip package files
        if path.endswith("__init__.py"):
            return False

        # Skip test files
        if path.startswith("test_"):
            return False

        if "/tests/" in path or path.startswith("tests/"):
            return False

        return True

    def plan(self, state):

        # -------------------------------------------------
        # STEP 1
        # Scan the project.
        # -------------------------------------------------

        if state.current_step == 1:
            return [
                {
                    "action": "project_search",
                    "args": {
                        "keyword": None,
                        "pattern": "*.py",
                    },
                }
            ]

        # -------------------------------------------------
        # STEP 2
        # Save discovered files.
        # -------------------------------------------------

        if state.last_action == "project_search":

            files = state.last_result.get("data", [])

            if not files:
                return []

            state.variables["remaining_files"] = files

            path = state.variables["remaining_files"].pop(0)
            state.variables["current_file"] = path

            return [
                {
                    "action": "read_code",
                    "args": {
                        "path": path,
                    },
                }
            ]

        # -------------------------------------------------
        # STEP 3
        # After reading a file.
        # -------------------------------------------------

        if state.last_action == "read_code":

            path = state.last_args["path"]

            if (
                path.startswith("test")
                or path.startswith("demo")
            ):
                return [
                    {
                        "action": "run_python",
                        "args": {
                            "path": path,
                        },
                    }
                ]

            remaining = state.variables.get("remaining_files", [])

            if not remaining:
                return []

            next_path = remaining.pop(0)
            state.variables["current_file"] = next_path

            return [
                {
                    "action": "read_code",
                    "args": {
                        "path": next_path,
                    },
                }
            ]
        # -------------------------------------------------
        # STEP 4
        # After executing.
        # -------------------------------------------------

        if state.last_action == "run_python":

            result = state.last_result.get("data", {})

            # Program succeeded
            if result.get("success", False):

                remaining = state.variables.get("remaining_files", [])

                if not remaining:
                    return []

                path = remaining.pop(0)
                state.variables["current_file"] = path

                return [
                    {
                        "action": "read_code",
                        "args": {
                            "path": path,
                        },
                    }
                ]

            # Program failed
            return [
                {
                    "action": "generate_patch",
                    "args": {
                        "path": state.last_args["path"],
                        "goal": result.get("stderr", ""),
                    },
                }
            ]

        # -------------------------------------------------
        # STEP 5
        # Patch generated.
        # -------------------------------------------------

        if state.last_action == "generate_patch":

            patched = (
                state.last_result
                .get("data", {})
                .get("patched")
            )

            return [
    {
                      "action": "apply_patch",
                      "args": {
                          "path": state.last_args["path"],
                           "patched_code": patched,
                    },
               }
       ]

        # -------------------------------------------------
        # STEP 6
        # Patch applied.
        # -------------------------------------------------

        if state.last_action == "apply_patch":

            return [
                {
                    "action": "run_python",
                    "args": {
                        "path": state.last_args["path"],
                    },
                }
            ]

        return []


agent_planner = AgentPlanner()
