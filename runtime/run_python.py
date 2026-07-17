import subprocess
import sys
import time
from pathlib import Path


class PythonRunner:
    """
    Executes Python files and captures the result.
    """

    def run(self, path, timeout=30):

        file = Path(path)

        if not file.exists():
            return {
                "success": False,
                "error": "File not found."
            }

        start = time.time()

        try:

            result = subprocess.run(
                [sys.executable, str(file)],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            elapsed = round(time.time() - start, 3)

            return {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "execution_time": elapsed
            }

        except subprocess.TimeoutExpired:

            return {
                "success": False,
                "error": f"Execution exceeded {timeout} seconds."
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


python_runner = PythonRunner()