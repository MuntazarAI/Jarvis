from brain.autodebugger import autodebugger

python_result = {
    "success": False,
    "stderr": """
Traceback (most recent call last):
  File "/home/muntazar/Projects/Jarvis/demo/error.py", line 5, in <module>
    hello()
  File "/home/muntazar/Projects/Jarvis/demo/error.py", line 2, in hello
    print(x)
NameError: name 'x' is not defined
"""
}

result = autodebugger.debug(python_result)

from pprint import pprint

pprint(result)