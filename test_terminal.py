from tools import registry

tool = registry.get("terminal")

print(tool.run(command="pwd"))
print()
print(tool.run(command="ls"))