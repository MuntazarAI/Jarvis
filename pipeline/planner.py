from intelligence.engineering_planner import engineering_planner


class EngineeringPlannerStage:
    """
    Uses the LLM to create an engineering plan.

    This stage never executes code.
    It only decides what should happen.
    """

    def plan(self, context):

        print("[Planner] Creating engineering plan...")

        project = context.project

        prompt = {
            "goal": context.request.goal,
            "project_files": project.get("python_files", []),
            "total_files": len(project.get("python_files", []))
        }

        context.plan = engineering_planner.plan(prompt)

        return context


engineering_planner_stage = EngineeringPlannerStage()