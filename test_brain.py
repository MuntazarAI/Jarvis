from brain.planner import Planner
from execution.executor import Executor

from tools.registry import ToolRegistry
from tools.memory_tool import MemoryTool

registry = ToolRegistry()
registry.register(MemoryTool())

planner = Planner()
executor = Executor(registry)


fake_llm = """
{
    "tool":"memory",
    "arguments":{
        "action":"search",
        "keyword":"Rust"
    }
}
"""

plan = planner.plan(fake_llm)

print("PLAN")
print(plan)

print()

print("RESULT")
print(executor.execute(plan))