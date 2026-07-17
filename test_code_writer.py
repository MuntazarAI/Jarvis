import tools
import tools.code_writer

from pathlib import Path
from tools.registry import registry

Path("demo").mkdir(exist_ok=True)

Path("demo/sample.py").write_text(
    "print('Hello')\n",
    encoding="utf-8"
)

tool = registry.get("code_writer")

print(tool.execute({
    "action": "append",
    "path": "demo/sample.py",
    "content": "print('Jarvis')\n"
}))

print()

print(tool.execute({
    "action": "replace",
    "path": "demo/sample.py",
    "old": "Hello",
    "new": "Hello World"
}))

print()

print(Path("demo/sample.py").read_text())