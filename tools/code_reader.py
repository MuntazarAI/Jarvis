from pathlib import Path

from tools.base import Tool
from tools.registry import registry


class CodeReader(Tool):

    name = "code_reader"

    description = "Read source code files."

    TEXT_EXTENSIONS = {
        ".py",
        ".txt",
        ".md",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".ini",
        ".cfg",
        ".html",
        ".css",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".c",
        ".h",
        ".hpp",
        ".rs",
        ".go",
        ".sh",
    }

    def run(
        self,
        path=None,
        start=None,
        end=None
    ):

        if not path:
            return {
                "success": False,
                "error": "Missing path."
            }

        file = Path(path)

        if not file.exists():

            return {
                "success": False,
                "error": "File does not exist."
            }

        if file.suffix.lower() not in self.TEXT_EXTENSIONS:

            return {
                "success": False,
                "error": "Unsupported file type."
            }

        try:

            text = file.read_text(encoding="utf-8")

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

        lines = text.splitlines()

        if start is not None:

            start = max(1, int(start))

        else:

            start = 1

        if end is not None:

            end = min(len(lines), int(end))

        else:

            end = len(lines)

        snippet = "\n".join(
            lines[start - 1:end]
        )

        return {
            "success": True,
            "path": str(file),
            "lines": len(lines),
            "start": start,
            "end": end,
            "content": snippet
        }


code_reader = CodeReader()

registry.register(code_reader)