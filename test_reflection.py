from intelligence.reflection import reflection

if __name__ == "__main__":
    tool_result = {
        "success": True,
        "stdout": "Hello Agent",
        "stderr": "",
        "returncode": 0
    }

    print(
        reflection.reply(
            "Run hello.py",
            tool_result
        )
    )
