import tools
import tools.project_tool

from tools.registry import registry

tool = registry.get("project")

print("\nFILES")
print(tool.execute({
    "action": "files"
})[:10])

print("\nCLASS: Brain")
print(tool.execute({
    "action": "class",
    "keyword": "Brain"
}))

print("\nFUNCTION: execute")
print(tool.execute({
    "action": "function",
    "keyword": "execute"
}))

print("\nIMPORT: ollama")
print(tool.execute({
    "action": "import",
    "keyword": "ollama"
}))

print("\nFILE: memory")
print(tool.execute({
    "action": "file",
    "keyword": "memory"
}))