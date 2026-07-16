class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def list(self):
        return list(self.tools.values())

    def schemas(self):
        return [tool.schema() for tool in self.tools.values()]


# Global registry instance
registry = ToolRegistry()