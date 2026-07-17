from pprint import pprint

from tools.code_reader import code_reader
from tools.code_analyzer import code_analyzer
from tools.error_analyzer import error_analyzer

from intelligence.ai_debugger import ai_debugger
from intelligence.patch_generator import patch_generator

traceback_text = """
Traceback (most recent call last):
  File "demo/error.py", line 5, in <module>
    hello()
  File "demo/error.py", line 2, in hello
    print(x)
NameError: name 'x' is not defined
"""

source = code_reader.run("demo/error.py")
analysis = code_analyzer.run("demo/error.py")
error = error_analyzer.run(traceback_text)
diagnosis = ai_debugger.diagnose({
    "source": source,
    "analysis": analysis,
    "error": error
})

patch = patch_generator.generate(
    source,
    analysis,
    error,
    diagnosis
)

pprint(patch)