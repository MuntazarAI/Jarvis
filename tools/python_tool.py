import subprocess
import tempfile
from pathlib import Path

from tools.base import Tool


class PythonTool(Tool):

    name = "python"

    description = (
        "Run Python code or execute Python files."
    )

    def run(self, action, **kwargs):

        try:

            if action == "run_code":

                code = kwargs["code"]

                with tempfile.NamedTemporaryFile(
                    suffix=".py",
                    delete=False,
                    mode="w",
                    encoding="utf-8"
                ) as f:

                    f.write(code)

                    filename = f.name

                result = subprocess.run(
                    ["python", filename],
                    capture_output=True,
                    text=True
                )

                Path(filename).unlink(missing_ok=True)

                return {
                    "success": result.returncode == 0,
                    "stdout": result.stdout.strip(),
                    "stderr": result.stderr.strip(),
                    "returncode": result.returncode
                }

            elif action == "run_file":

                result = subprocess.run(
                    ["python", kwargs["path"]],
                    capture_output=True,
                    text=True
                )

                return {
                    "success": result.returncode == 0,
                    "stdout": result.stdout.strip(),
                    "stderr": result.stderr.strip(),
                    "returncode": result.returncode
                }

            else:

                return {
                    "success": False,
                    "error": f"Unknown action '{action}'"
                }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


python_tool = PythonTool()