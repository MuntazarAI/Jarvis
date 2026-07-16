from tools.registry import registry

from tools.memory_tool import MemoryTool
from tools.terminal import TerminalTool
from tools.filesystem import FileSystemTool
from tools.python_tool import PythonTool

registry.register(MemoryTool())
registry.register(TerminalTool())
registry.register(FileSystemTool())
registry.register(PythonTool())