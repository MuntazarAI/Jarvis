import ast
import json
from pathlib import Path


class ProjectMemory:
    """
    Scans the Jarvis project and builds a searchable index.
    """

    def __init__(self, root="."):
        self.root = Path(root)

    def scan(self):
        project = []

        for file in self.root.rglob("*.py"):

            # Ignore virtual environments and cache
            if ".venv" in file.parts:
                continue

            if "__pycache__" in file.parts:
                continue

            info = self._analyze(file)
            project.append(info)

        project.sort(key=lambda x: x["path"])

        return project

    def _analyze(self, path):

        info = {
            "name": path.name,
            "path": str(path),
            "size": path.stat().st_size,
            "classes": [],
            "functions": [],
            "imports": []
        }

        try:

            source = path.read_text(encoding="utf-8")

            tree = ast.parse(source)

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    info["classes"].append(node.name)

                elif isinstance(node, ast.FunctionDef):
                    info["functions"].append(node.name)

                elif isinstance(node, ast.Import):
                    for n in node.names:
                        info["imports"].append(n.name)

                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    info["imports"].append(module)

        except Exception as e:
            info["error"] = str(e)

        return info

    def build_index(self):

        project = self.scan()

        Path("data").mkdir(exist_ok=True)

        output = Path("data/project_index.json")

        with output.open("w", encoding="utf-8") as f:
            json.dump(project, f, indent=4)

        return {
            "success": True,
            "files": len(project),
            "index": str(output)
        }


project_memory = ProjectMemory()