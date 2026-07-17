from brain.brain import Brain
from execution.executor import executor
from intelligence.reflection import reflection
from brain.formatter import format_tool_result
from brain.validator import validator

brain = Brain()

while True:

    text = input("\nYou: ")

    if text.lower() == "exit":
        break

    plan = brain.think(text)
    plan = validator.validate(plan)
    
    print("\nPLAN")
    print(plan)

    result = executor.execute(plan)

    print("\nRESULT")
    print(format_tool_result(result))

    answer = reflection.reply(text, result)

    print("\nJarvis:")
    print(answer)