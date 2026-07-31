import tools
import tools.code_reader

from tools.registry import registry

if __name__ == "__main__":
    tool = registry.get("code_reader")

    print(tool.execute({
        "path": "brain/brain.py"
    }))

    print()

    print(tool.execute({
        "path": "brain/brain.py",
        "start": 1,
        "end": 15
    }))
