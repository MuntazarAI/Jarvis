import ast
from pathlib import Path

from tools.base import Tool
from tools.registry import registry


class CodeAnalyzer(Tool):

    name = "code_analyzer"

    description = "Analyze Python source code."

    def run(self, path=None):

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

        try:
            source = file.read_text(encoding="utf-8")
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

        try:
            tree = ast.parse(source)
        except Exception as e:
            return {
                "success": False,
                "error": f"Syntax Error: {e}"
            }

        classes = []
        functions = []
        imports = []
        todos = []
        docstrings = {}

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                classes.append(node.name)

                docstrings[node.name] = ast.get_docstring(node)

            elif isinstance(node, ast.FunctionDef):

                functions.append({
                    "name": node.name,
                    "line": node.lineno,
                    "arguments": [
                        arg.arg for arg in node.args.args
                    ]
                })

                docstrings[node.name] = ast.get_docstring(node)

            elif isinstance(node, ast.Import):

                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                imports.append(module)

        for number, line in enumerate(source.splitlines(), start=1):

            upper = line.upper()

            if "TODO" in upper or "FIXME" in upper:

                todos.append({
                    "line": number,
                    "text": line.strip()
                })

        return {
            "success": True,
            "file": str(file),
            "lines": len(source.splitlines()),
            "classes": classes,
            "functions": functions,
            "imports": sorted(set(imports)),
            "todos": todos,
            "docstrings": docstrings
        }


code_analyzer = CodeAnalyzer()

registry.register(code_analyzer)