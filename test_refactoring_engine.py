from pprint import pprint

from brain.refactoring_engine import refactoring_engine

result = refactoring_engine.refactor(
    "Fix every NameError in the project."
)

print()

print("=" * 80)
print("PLAN")
print("=" * 80)

pprint(result["plan"])

print()

print("=" * 80)
print("FILES ANALYZED")
print("=" * 80)

print(len(result["results"]))

print()

for item in result["results"][:3]:

    print("-" * 60)

    print(item["file"])

    pprint(item["debug"])

    pprint(item["patch"])