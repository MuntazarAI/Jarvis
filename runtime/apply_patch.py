import ast
import shutil
from pathlib import Path


class PatchApplier:
    """
    Safely applies generated code.

    Workflow

        backup
            ↓
        syntax check
            ↓
        write
            ↓
        rollback on failure
    """

    def apply(self, path, patched_code):

        path = Path(path)

        if not path.exists():

            return {
                "success": False,
                "error": "File does not exist."
            }

        backup = path.with_suffix(path.suffix + ".bak")

        shutil.copy2(path, backup)

        try:

            ast.parse(patched_code)

        except SyntaxError as e:

            return {
                "success": False,
                "error": f"SyntaxError: {e}",
                "backup": str(backup)
            }

        try:

            path.write_text(
                patched_code,
                encoding="utf-8"
            )

        except Exception as e:

            shutil.copy2(backup, path)

            return {
                "success": False,
                "error": str(e)
            }

        return {
            "success": True,
            "path": str(path),
            "backup": str(backup)
        }

    def restore(self, path):

        path = Path(path)

        backup = path.with_suffix(path.suffix + ".bak")

        if not backup.exists():

            return {
                "success": False,
                "error": "Backup not found."
            }

        shutil.copy2(backup, path)

        return {
            "success": True,
            "path": str(path)
        }


patch_applier = PatchApplier()