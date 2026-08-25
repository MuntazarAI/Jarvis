from pprint import pprint

from intelligence.engineering_planner import engineering_planner


if __name__ == "__main__":
    plan = engineering_planner.plan(
        "Fix every NameError in the project."
    )

    pprint(plan)
