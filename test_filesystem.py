from tools.filesystem import FileSystemTool

fs = FileSystemTool()

print(fs.run(
    action="mkdir",
    path="demo"
))

print(fs.run(
    action="write",
    path="demo/test.txt",
    content="Hello Jarvis!"
))

print(fs.run(
    action="read",
    path="demo/test.txt"
))

print(fs.run(
    action="list",
    path="demo"
))

print(fs.run(
    action="search",
    path=".",
    keyword="test"
))