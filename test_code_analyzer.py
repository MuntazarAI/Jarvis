import tools
import tools.code_analyzer

from pprint import pprint
from tools.registry import registry

if __name__ == "__main__":
    tool = registry.get("code_analyzer")

    result = tool.execute({
        "path": "brain/brain.py"
    })

    pprint(result)
