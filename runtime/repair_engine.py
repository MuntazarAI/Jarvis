from runtime.run_python import python_runner
from runtime.generate_patch import patch_generator
from runtime.apply_patch import patch_applier


class RepairEngine:
    """
    Autonomous repair engine.

    Workflow

        Run file
            ↓
        Failed?
            ↓
        Generate patch
            ↓
        Apply patch
            ↓
        Run again
            ↓
        Repeat
    """

    def repair(
        self,
        path,
        goal,
        max_iterations=5,
    ):

        history = []

        for iteration in range(max_iterations):

            run = python_runner.run(path)

            history.append({
                "iteration": iteration + 1,
                "stage": "run",
                "result": run
            })

            if run["success"]:

                return {
                    "success": True,
                    "iterations": iteration,
                    "history": history
                }

            patch = patch_generator.generate(
                path,
                goal + "\n\nError:\n" + run["stderr"]
            )

            history.append({
                "iteration": iteration + 1,
                "stage": "generate_patch",
                "result": patch
            })

            if not patch["success"]:

                return {
                    "success": False,
                    "history": history
                }

            applied = patch_applier.apply(
                path,
                patch["patched"]
            )

            history.append({
                "iteration": iteration + 1,
                "stage": "apply_patch",
                "result": applied
            })

            if not applied["success"]:

                return {
                    "success": False,
                    "history": history
                }

        return {
            "success": False,
            "reason": "Maximum iterations reached.",
            "history": history
        }


repair_engine = RepairEngine()