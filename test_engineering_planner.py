from pprint import pprint

from intelligence.engineering_planner import engineering_planner


plan = engineering_planner.plan(
    "Fix every NameError in the project."
)

pprint(plan)