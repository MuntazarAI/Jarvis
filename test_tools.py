from tools.manager import ToolManager
from tools.memory_tool import MemoryTool


manager = ToolManager()

manager.register(MemoryTool())


print(
    manager.run(
        "memory",
        action="remember",
        data={
            "profile": {
                "favorite_editor": "VS Code"
            }
        }
    )
)

print(
    manager.run(
        "memory",
        action="search",
        query="editor"
    )
)