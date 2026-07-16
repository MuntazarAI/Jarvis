from brain.multiexecutor import multiexecutor

plan = {
    "steps": [
        {
            "tool": "filesystem",
            "arguments": {
                "action": "mkdir",
                "path": "AgentTest"
            }
        },
        {
            "tool": "filesystem",
            "arguments": {
                "action": "write",
                "path": "AgentTest/hello.py",
                "content": "print('Hello Agent')"
            }
        },
        {
            "tool": "python",
            "arguments": {
                "action": "run_file",
                "path": "AgentTest/hello.py"
            }
        }
    ]
}

print(multiexecutor.execute(plan))