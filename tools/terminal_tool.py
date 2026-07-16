from tools.base import Tool
from tools.terminal import terminal


class TerminalTool(Tool):

    name = "terminal"

    description = "Execute terminal commands."

    def run(self, command, **kwargs):
        return terminal.run(command)