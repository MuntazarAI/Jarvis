import subprocess
import sys
import time
from pathlib import Path


class PythonRunner:
    """
    Executes a Python file inside the project root.

    Returns a dictionary:

    {
        "success": bool,
        "returncode": int,
        "stdout": str,
        "stderr": str,
        "execution_time": float
    }
    """

    def run(self, path, timeout=30):

        file = Path(path)

        if not file.exists():
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"File not found: {file}",
                "execution_time": 0,
            }

        start = time.time()

        try:

            result = subprocess.run(
                [sys.executable, "-m", file.with_suffix("").as_posix().replace("/", ".")],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            elapsed = round(time.time() - start, 3)

            return {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "execution_time": elapsed,
            }

        except subprocess.TimeoutExpired:

            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Execution exceeded {timeout} seconds.",
                "execution_time": round(time.time() - start, 3),
            }

        except Exception as e:

            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "execution_time": round(time.time() - start, 3),
            }


python_runner = PythonRunner()