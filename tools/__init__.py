from tools.registry import registry

from tools.memory_tool import MemoryTool
from tools.terminal import TerminalTool
from tools.filesystem import FileSystemTool
from tools.python_tool import PythonTool
from tools.project_tool import ProjectTool
from tools.code_reader import CodeReader
from tools.code_analyzer import CodeAnalyzer
from tools.code_writer import CodeWriter
from tools.error_analyzer import ErrorAnalyzer

registry.register(MemoryTool())
registry.register(TerminalTool())
registry.register(FileSystemTool())
registry.register(PythonTool())
registry.register(ProjectTool())
registry.register(CodeReader())
registry.register(CodeAnalyzer())
registry.register(CodeWriter())
registry.register(ErrorAnalyzer())