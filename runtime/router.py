"""
Runtime tool router.

Every engineering action goes through this router.

All tools return RuntimeResult objects.
"""

from runtime.result import RuntimeResult

from runtime.project_search import project_search
from runtime.read_code import read_code
from runtime.write_code import write_code
from runtime.run_python import python_runner
from runtime.run_terminal import terminal_runner
from runtime.apply_patch import patch_applier
from runtime.generate_patch import patch_generator
from runtime.test_runner import test_runner


class RuntimeRouter:

    def __init__(self):

        self.tools = {

            "project_search": project_search.search,

            "read_code": read_code.read,

            "write_code": write_code.write,

            "run_python": python_runner.run,

            "run_terminal": terminal_runner.run,

            "generate_patch": patch_generator.generate,

            "apply_patch": patch_applier.apply,

            "test": test_runner.run,

        }

    def available_tools(self):

        return sorted(self.tools.keys())
    def execute(self, action, **kwargs):

        tool = self.tools.get(action)

        if tool is None:
            return RuntimeResult.fail(
                action,
                f"Unknown tool: {action}",
            )

        try:

            result = tool(**kwargs)

            if isinstance(result, RuntimeResult):
                return result

            if isinstance(result, dict):

                if result.get("success", False):

                    return RuntimeResult.ok(
                        action,
                        data=result,
                    )

                return RuntimeResult.fail(
                    action,
                    result.get(
                        "error",
                        result.get(
                            "stderr",
                            "Unknown error",
                        ),
                    ),
                    data=result,
                )

            return RuntimeResult.ok(
                action,
                data=result,
            )

        except Exception as e:

            return RuntimeResult.fail(
                action,
                str(e),
            )


runtime_router = RuntimeRouter()