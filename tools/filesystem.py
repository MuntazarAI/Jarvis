from pathlib import Path
import shutil

from tools.base import Tool


class FileSystemTool(Tool):

    name = "filesystem"

    description = (
        "Read, write, create, append, delete, rename, copy, move, "
        "list, search files and directories."
    )

    def run(self, action, **kwargs):

        try:

            if action == "read":

                path = Path(kwargs["path"])

                return path.read_text(encoding="utf-8")

            elif action == "write":

                path = Path(kwargs["path"])

                path.parent.mkdir(parents=True, exist_ok=True)

                path.write_text(
                    kwargs.get("content", ""),
                    encoding="utf-8"
                )

                return {"success": True}

            elif action == "append":

                path = Path(kwargs["path"])

                path.parent.mkdir(parents=True, exist_ok=True)

                with open(path, "a", encoding="utf-8") as f:
                    f.write(kwargs.get("content", ""))

                return {"success": True}

            elif action == "create":

                path = Path(kwargs["path"])

                path.parent.mkdir(parents=True, exist_ok=True)

                path.touch(exist_ok=True)

                return {"success": True}

            elif action == "delete":

                path = Path(kwargs["path"])

                if path.is_dir():
                    shutil.rmtree(path)
                elif path.exists():
                    path.unlink()

                return {"success": True}

            elif action == "rename":

                src = Path(kwargs["source"])
                dst = Path(kwargs["destination"])

                src.rename(dst)

                return {"success": True}

            elif action == "copy":

                src = Path(kwargs["source"])
                dst = Path(kwargs["destination"])

                if src.is_dir():
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, dst)

                return {"success": True}

            elif action == "move":

                shutil.move(
                    kwargs["source"],
                    kwargs["destination"]
                )

                return {"success": True}

            elif action == "mkdir":

                Path(kwargs["path"]).mkdir(
                    parents=True,
                    exist_ok=True
                )

                return {"success": True}

            elif action == "list":

                path = Path(kwargs.get("path", "."))

                return [
                    str(item)
                    for item in sorted(path.iterdir())
                ]

            elif action == "exists":

                return {
                    "exists": Path(kwargs["path"]).exists()
                }

            elif action == "search":

                root = Path(kwargs.get("path", "."))

                keyword = kwargs["keyword"].lower()

                results = []

                for item in root.rglob("*"):

                    if keyword in item.name.lower():
                        results.append(str(item))

                return results

            return {
                "error": f"Unknown action '{action}'"
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }