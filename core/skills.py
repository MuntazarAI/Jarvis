"""
skills.py

Registers every skill Jarvis can use.
"""

from core.browser import google_search
from core.system import open_application


class SkillManager:

    def __init__(self):

        self.skills = {}

    def register(self, name, function):

        self.skills[name] = function

    def execute(self, name, argument):

        if name not in self.skills:
            return f"Skill '{name}' not found."

        return self.skills[name](argument)

    def list_skills(self):

        return sorted(self.skills.keys())


skills = SkillManager()


skills.register("browser", google_search)
skills.register("system", open_application)
