import ast
from pathlib import Path


class DependencyGraph:
    """
    Builds a dependency graph for a Python project.

    Stores:

    graph[file] = {
        "imports": [],
        "classes": [],
        "functions": [],
        "used_by": []
    }
    """

    IGNORE = {
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
    }

    def __init__(self):
        self.graph = {}

    def build(self, root="."):

        root = Path(root)
        self.graph = {}

        python_files = []

        for path in root.rglob("*.py"):

            if any(part in self.IGNORE for part in path.parts):
                continue

            python_files.append(path)

        #
        # First pass
        #

        for file in python_files:

            relative = str(file.relative_to(root))

            try:
                source = file.read_text(encoding="utf-8")
                tree = ast.parse(source)

            except Exception:
                continue

            imports = []
            classes = []
            functions = []

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:
                        imports.append(alias.name)

                elif isinstance(node, ast.ImportFrom):

                    imports.append(node.module or "")

                elif isinstance(node, ast.ClassDef):

                    classes.append(node.name)

                elif isinstance(node, ast.FunctionDef):

                    functions.append(node.name)

            self.graph[relative] = {
                "imports": sorted(set(imports)),
                "classes": sorted(classes),
                "functions": sorted(functions),
                "used_by": []
            }

        #
        # Reverse dependency graph
        #

        for file, info in self.graph.items():

            for imported in info["imports"]:

                imported_path = imported.replace(".", "/") + ".py"

                for other in self.graph:

                    if other.endswith(imported_path):
                        self.graph[other]["used_by"].append(file)

        return self.graph


dependency_graph = DependencyGraph()