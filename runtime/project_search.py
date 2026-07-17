from pathlib import Path


class ProjectSearch:
    """
    Searches a project for files by filename
    or by text contained inside files.
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

    def search(
        self,
        root=".",
        keyword=None,
        pattern="*.py",
    ):
        root = Path(root)

        matches = []

        keyword_lower = keyword.lower() if keyword else None

        for file in root.rglob(pattern):

            if any(part in self.IGNORE for part in file.parts):
                continue

            relative = str(file.relative_to(root))

            #
            # No keyword → return every file
            #

            if keyword_lower is None:
                matches.append(relative)
                continue

            #
            # Match filename
            #

            if keyword_lower in file.name.lower():
                matches.append(relative)
                continue

            #
            # Match file contents
            #

            try:
                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                if keyword_lower in text.lower():
                    matches.append(relative)

            except Exception:
                pass

        return sorted(matches)


project_search = ProjectSearch()