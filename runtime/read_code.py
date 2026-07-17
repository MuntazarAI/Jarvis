from pathlib import Path


class CodeReader:
    """
    Reads source code from files.
    """

    def read(self, path):

        file = Path(path)

        if not file.exists():
            return {
                "success": False,
                "error": "File not found."
            }

        if not file.is_file():
            return {
                "success": False,
                "error": "Not a file."
            }

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            return {
                "success": True,
                "path": str(file),
                "content": content,
                "lines": len(content.splitlines()),
                "characters": len(content)
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


code_reader = CodeReader()