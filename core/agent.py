"""
agent.py

Central brain of Jarvis.
"""

from core.planner import planner
from core.chat import ask
from core.skills import skills


class Agent:

    def handle(self, prompt):

        plan = planner.create_plan(prompt)

        if plan.intent == "system":
            return skills.execute("system", plan.target)

        if plan.intent == "browser":
            return skills.execute("browser", plan.target)

        return ask(prompt)


agent = Agent()
