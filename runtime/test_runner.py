import json
import sys

from runtime.run_terminal import terminal_runner


class TestRunner:
    """
    Runs pytest or plain Python test scripts.

    Automatically detects whether a file is a real pytest test
    or just a standalone script.
    """

    def run(self, target=".", pytest_args="-q"):
        """
        Run pytest.

        target:
            .
            tests
            test_file.py
        """

        command = (
            f'"{sys.executable}" '
            f'-m pytest {pytest_args} "{target}"'
        )

        result = terminal_runner.run(command, timeout=300)

        return self._format(command, result)

    def run_file(self, file):
        """
        Run a single file.

        If pytest collects zero tests,
        automatically execute it as a normal script.
        """

        result = self.run(file)

        #
        # Exit code 5 = no tests collected
        #

        if result["returncode"] == 5:

            command = f'"{sys.executable}" "{file}"'

            script_result = terminal_runner.run(
                command,
                timeout=300
            )

            return self._format(command, script_result)

        return result

    def run_script(self, file):
        """
        Always run as a Python script.
        """

        command = f'"{sys.executable}" "{file}"'

        result = terminal_runner.run(
            command,
            timeout=300
        )

        return self._format(command, result)

    def run_all(self):
        """
        Run every pytest test.

        Uses a longer timeout because large projects
        can take several minutes.
        """

        return self.run(".", "-q")

    def summary(self, result):

        return {
            "success": result["success"],
            "returncode": result["returncode"],
            "execution_time": result["execution_time"],
            "stdout_lines": len(result["stdout"].splitlines()),
            "stderr_lines": len(result["stderr"].splitlines()),
        }

    def to_json(self, result):

        return json.dumps(result, indent=4)

    def _format(self, command, result):

        return {
            "success": result.get("success", False),
            "command": command,
            "returncode": result.get("returncode", -1),
            "stdout": result.get("stdout", ""),
            "stderr": result.get("stderr", ""),
            "execution_time": result.get("execution_time", 0),
        }


test_runner = TestRunner()