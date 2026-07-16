"""
tools.py

Central registry for every tool Jarvis can use.
"""

from core.system import open_application
from core.browser import google_search


class ToolManager:

    def __init__(self):

        self.tools = {
            "system": open_application,
            "browser": google_search,
        }

    def has_tool(self, name: str) -> bool:
        return name in self.tools

    def execute(self, tool: str, argument: str):

        if tool not in self.tools:
            return f"Unknown tool: {tool}"

        return self.tools[tool](argument)


tool_manager = ToolManager()
