from runtime.project_search import project_search
from runtime.read_code import code_reader
from runtime.write_code import code_writer
from runtime.run_python import python_runner


class RuntimeRouter:
    """
    Routes engineering actions to the proper runtime tool.
    """

    def execute(self, step):

        action = step.get("action")
        args = step.get("args", {})

        try:

            if action == "project_search":

                return project_search.search(
                    root=args.get("path", "."),
                    keyword=args.get("keyword"),
                    pattern=args.get("pattern", "*.py")
                )

            elif action == "read_code":

                return code_reader.read(
                    args["path"]
                )

            elif action == "write_code":

                return code_writer.write(
                    args["path"],
                    args["content"]
                )

            elif action == "run_python":

                return python_runner.run(
                    args["path"]
                )

            else:

                return {
                    "success": False,
                    "error": f"Unknown runtime action: {action}"
                }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


runtime_router = RuntimeRouter()