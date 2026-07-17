from pprint import pprint

from brain.ai_debugger import ai_debugger
from tools.error_analyzer import error_analyzer
from tools.code_reader import code_reader
from tools.code_analyzer import code_analyzer

TRACEBACK = """
Traceback (most recent call last):
  File "demo/error.py", line 4, in <module>
    hello()
  File "demo/error.py", line 2, in hello
    print(x)
NameError: name 'x' is not defined
"""

error = error_analyzer.execute({
    "traceback": TRACEBACK
})

source = code_reader.execute({
    "path": "demo/error.py"
})

analysis = code_analyzer.execute({
    "path": "demo/error.py"
})

debug_data = {
    "error": error,
    "source": source,
    "analysis": analysis
}

result = ai_debugger.diagnose(debug_data)

pprint(result)