import tools
import tools.error_analyzer

from pprint import pprint
from tools.registry import registry

traceback = """
Traceback (most recent call last):
  File "/home/muntazar/Projects/Jarvis/test.py", line 10, in <module>
    hello()
  File "/home/muntazar/Projects/Jarvis/test.py", line 5, in hello
    print(x)
NameError: name 'x' is not defined
"""

tool = registry.get("error_analyzer")

pprint(tool.execute({
    "traceback": traceback
}))