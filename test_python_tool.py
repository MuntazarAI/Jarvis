from tools.python_tool import PythonTool

py = PythonTool()

print(py.run(
    action="run_code",
    code="""
print("Hello from Jarvis!")
"""
))

print(py.run(
    action="run_code",
    code="""
for i in range(5):
    print(i)
"""
))