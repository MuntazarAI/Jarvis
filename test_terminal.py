from tools import registry

if __name__ == "__main__":
    tool = registry.get("terminal")

    print(tool.run(command="pwd"))
    print()
    print(tool.run(command="ls"))
