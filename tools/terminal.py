import subprocess
import re
import tempfile
import os

from tools.base import Tool


class TerminalTool(Tool):

    name = "terminal"

    description = "Execute terminal commands."

    def run(self, command):

        # Detect patterns like "... in a temporary Python script" and run the code as a temp .py file
        try:
            m = re.search(r"(.+?)\s+in a temporary\s+python\s+script", command, flags=re.I)
            if m:
                code_fragment = m.group(1).strip()
                # remove leading verbs like 'Run' or 'Execute'
                code_fragment = re.sub(r'^(Run|Execute)\s+', '', code_fragment, flags=re.I).strip()
                # strip surrounding quotes if present
                if (code_fragment.startswith('"') and code_fragment.endswith('"')) or (code_fragment.startswith("'") and code_fragment.endswith("'")):
                    code_fragment = code_fragment[1:-1]

                # Write to temporary python file and execute
                fd, path = tempfile.mkstemp(suffix='.py', text=True)
                with os.fdopen(fd, 'w') as f:
                    f.write(code_fragment + '\n')

                try:
                    result = subprocess.run(
                        ['python3', path],
                        capture_output=True,
                        text=True
                    )
                    return {
                        "success": result.returncode == 0,
                        "stdout": result.stdout.strip(),
                        "stderr": result.stderr.strip(),
                        "returncode": result.returncode
                    }
                finally:
                    try:
                        os.remove(path)
                    except Exception:
                        pass

            # Fallback: run the command directly in shell
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