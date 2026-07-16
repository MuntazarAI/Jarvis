import subprocess

from tools.base import Tool


class TerminalTool(Tool):

    name = "terminal"

    description = "Execute terminal commands."

    def run(self, command):

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "returncode": result.returncode
            }

        except Exception as e:
            return {
                "success": False,
                "stderr": str(e)
            }