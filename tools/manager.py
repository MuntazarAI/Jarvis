class ToolManager:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.values())

    def run(self, name, **kwargs):

        tool = self.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool: {name}")

        return tool.run(**kwargs)