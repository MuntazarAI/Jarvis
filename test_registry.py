from tools.registry import ToolRegistry
from tools.memory_tool import MemoryTool

registry = ToolRegistry()

registry.register(MemoryTool())

print("Available tools:\n")

for tool in registry.schemas():
    print(tool)

print("\nSearching memory...\n")

memory_tool = registry.get("memory")

print(
    memory_tool.run(
        action="search",
        keyword="Rust"
    )
)
