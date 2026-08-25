import re

from tools.base import Tool
from tools.registry import registry


class ErrorAnalyzer(Tool):

    name = "error_analyzer"

    description = "Analyze Python tracebacks."

    FILE_PATTERN = re.compile(
        r'File "(.+?)", line (\d+), in (.+)'
    )

    ERROR_PATTERN = re.compile(
        r"([A-Za-z_]+Error): (.+)"
    )

    def run(self, traceback=None):

        if not traceback:

            return {
                "success": False,
                "error": "Missing traceback."
            }

        files = []

        for match in self.FILE_PATTERN.finditer(traceback):

            files.append({
                "path": match.group(1),
                "line": int(match.group(2)),
                "function": match.group(3)
            })

        error_match = self.ERROR_PATTERN.search(traceback)

        if error_match:

            error_type = error_match.group(1)
            message = error_match.group(2)

        else:

            error_type = None
            message = None

        return {
            "success": True,
            "frames": files,
            "error_type": error_type,
            "message": message,
            "last_frame": files[-1] if files else None
        }


error_analyzer = ErrorAnalyzer()

registry.register(error_analyzer)