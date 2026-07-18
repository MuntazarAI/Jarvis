from pathlib import Path


class WriteCode:
    """
    Runtime tool for writing source code.
    """

    def write(self, path, content):

        file = Path(path)

        try:

            file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            old_content = ""

            if file.exists():

                old_content = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

            file.write_text(
                content,
                encoding="utf-8",
            )

            return {
                "success": True,
                "path": str(file),
                "bytes_written": len(content.encode("utf-8")),
                "lines": len(content.splitlines()),
                "changed": old_content != content,
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e),
            }


write_code = WriteCode()