from pathlib import Path


class ProjectScanner:
    """
    Builds an overview of the entire project.
    """

    IGNORE = {
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
        "node_modules",
    }

    CODE_EXTENSIONS = {
        ".py",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".md",
    }

    def scan(self, root="."):

        root = Path(root)

        result = {
            "root": str(root.resolve()),
            "files": [],
            "python_files": [],
            "tests": [],
            "directories": [],
        }

        for path in root.rglob("*"):

            if any(part in self.IGNORE for part in path.parts):
                continue

            if path.is_dir():
                result["directories"].append(str(path))
                continue

            if path.suffix.lower() not in self.CODE_EXTENSIONS:
                continue

            relative = str(path.relative_to(root))

            result["files"].append(relative)

            if path.suffix == ".py":
                result["python_files"].append(relative)

                if (
                    path.name.startswith("test_")
                    or "/tests/" in relative
                    or relative.startswith("tests/")
                ):
                    result["tests"].append(relative)

        result["files"].sort()
        result["python_files"].sort()
        result["tests"].sort()

        return result


project_scanner = ProjectScanner()