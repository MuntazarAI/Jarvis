from intelligence.engineering_planner import engineering_planner
from analysis.affected_files import affected_files
from intelligence.patch_generator import patch_generator
from intelligence.ai_debugger import ai_debugger

from tools.code_reader import code_reader
from tools.code_analyzer import code_analyzer


class RefactoringEngine:
    """
    Coordinates project-wide refactoring.

    Workflow:

    Goal
      ↓
    Planner
      ↓
    Dependency Analysis
      ↓
    Read Files
      ↓
    Analyze
      ↓
    Generate Patch
    """

    def refactor(self, goal, root="."):

        affected_files.build(root)

        plan = engineering_planner.plan(goal)

        results = []

        graph = affected_files.graph

        for file in graph:

            source = code_reader.run(file)

            if not source["success"]:
                continue

            analysis = code_analyzer.run(file)

            # No traceback yet, so create an empty error object
            error = {
                "error_type": "",
                "message": ""
            }

            diagnosis = ai_debugger.diagnose(
                {
                    "goal": goal,
                    "source": source,
                    "analysis": analysis,
                    "error": error
                }
            )

            patch = patch_generator.generate(
                source,
                analysis,
                error,
                diagnosis
            )

            results.append(
                {
                    "file": file,
                    "analysis": analysis,
                    "diagnosis": diagnosis,
                    "patch": patch
                }
            )

        return {
            "goal": goal,
            "plan": plan,
            "results": results
        }


refactoring_engine = RefactoringEngine()