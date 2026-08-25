import subprocess
import time
from pathlib import Path


class TerminalRunner:
    """
    Executes terminal commands and captures stdout,
    stderr and execution time.
    """

    def run(
        self,
        command,
        cwd=".",
        timeout=60,
        shell=True,
    ):

        cwd = Path(cwd)

        start = time.time()

        try:

            completed = subprocess.run(
                command,
                shell=shell,
                cwd=str(cwd),
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            elapsed = round(time.time() - start, 3)

            return {
                "success": completed.returncode == 0,
                "command": command,
                "cwd": str(cwd.resolve()),
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "execution_time": elapsed,
            }

        except subprocess.TimeoutExpired as e:

            elapsed = round(time.time() - start, 3)

            return {
                "success": False,
                "command": command,
                "cwd": str(cwd.resolve()),
                "returncode": -1,
                "stdout": e.stdout or "",
                "stderr": f"Timeout after {timeout} seconds.",
                "execution_time": elapsed,
            }

        except Exception as e:

            elapsed = round(time.time() - start, 3)

            return {
                "success": False,
                "command": command,
                "cwd": str(cwd.resolve()),
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "execution_time": elapsed,
            }


terminal_runner = TerminalRunner()