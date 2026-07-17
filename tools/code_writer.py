from pathlib import Path
import shutil

from tools.base import Tool
from tools.registry import registry


class CodeWriter(Tool):

    name = "code_writer"

    description = "Safely modify source code files."

    def backup(self, path):

        backup = path.with_suffix(path.suffix + ".bak")

        shutil.copy2(path, backup)

        return str(backup)

    def run(
        self,
        action=None,
        path=None,
        content=None,
        old=None,
        new=None,
        line=None
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
                "error": "File not found."
            }

        self.backup(file)

        text = file.read_text(encoding="utf-8")

        if action == "write":

            file.write_text(content, encoding="utf-8")

        elif action == "append":

            file.write_text(
                text + content,
                encoding="utf-8"
            )

        elif action == "replace":

            if old not in text:

                return {
                    "success": False,
                    "error": "Target text not found."
                }

            file.write_text(
                text.replace(old, new),
                encoding="utf-8"
            )

        elif action == "insert":

            lines = text.splitlines()

            if line is None:

                return {
                    "success": False,
                    "error": "Missing line number."
                }

            index = max(0, min(len(lines), int(line) - 1))

            lines.insert(index, content)

            file.write_text(
                "\n".join(lines),
                encoding="utf-8"
            )

        elif action == "delete":

            lines = text.splitlines()

            start = int(line)

            end = start

            if new is not None:

                end = int(new)

            del lines[start - 1:end]

            file.write_text(
                "\n".join(lines),
                encoding="utf-8"
            )

        else:

            return {
                "success": False,
                "error": "Unknown action."
            }

        return {
            "success": True,
            "action": action,
            "path": str(file)
        }


code_writer = CodeWriter()

registry.register(code_writer)