import json
from pathlib import Path

from tools.base import Tool
from tools.registry import registry


class ProjectTool(Tool):
    """
    Search the indexed Jarvis project.
    """

    name = "project"

    description = "Search files, classes, functions and imports in the Jarvis project."

    INDEX_FILE = Path("data/project_index.json")

    def _load(self):
        if not self.INDEX_FILE.exists():
            return []

        with self.INDEX_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)

    def run(self, action=None, keyword=None):

        if action is None:
            return {"success": False, "error": "Missing action."}

        data = self._load()

        if action == "files":

            return [
                file["path"]
                for file in data
            ]

        if keyword is None:
            return {"success": False, "error": "Missing keyword."}

        keyword = keyword.lower()

        results = []

        for file in data:

            if action == "file":

                if keyword in file["name"].lower():

                    results.append(file)

            elif action == "class":

                for cls in file["classes"]:

                    if keyword in cls.lower():

                        results.append(file)

                        break

            elif action == "function":

                for fn in file["functions"]:

                    if keyword in fn.lower():

                        results.append(file)

                        break

            elif action == "import":

                for imp in file["imports"]:

                    if keyword in imp.lower():

                        results.append(file)

                        break

        return results


project_tool = ProjectTool()

registry.register(project_tool)