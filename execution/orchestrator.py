from analysis.project_scanner import project_scanner
from analysis.dependency_graph import dependency_graph
from analysis.affected_files import affected_files

from intelligence.engineering_planner import engineering_planner
from intelligence.ai_debugger import ai_debugger
from intelligence.patch_generator import patch_generator

from execution.executor import executor


class EngineeringOrchestrator:
    """
    Coordinates the complete engineering pipeline.

        User Request
              │
              ▼
        Scan Project
              │
              ▼
      Build Dependency Graph
              │
              ▼
      Determine Affected Files
              │
              ▼
         AI Diagnosis
              │
              ▼
      Engineering Planner
              │
              ▼
        Patch Generator
              │
              ▼
           Executor
    """

    def prepare(self, root="."):
        project = project_scanner.scan(root)

        graph = dependency_graph.build(root)

        affected = affected_files.build(root)

        return {
            "project": project,
            "graph": graph,
            "affected": affected,
        }

    def repair(self, request, code_context):
        diagnosis = ai_debugger.diagnose(code_context)

        plan = engineering_planner.plan(
            request=request,
            diagnosis=diagnosis,
        )

        patches = patch_generator.generate(
            request=request,
            diagnosis=diagnosis,
            plan=plan,
        )

        return {
            "diagnosis": diagnosis,
            "plan": plan,
            "patches": patches,
        }

    def execute(self, plan):
        return executor.execute(plan)


engineering_orchestrator = EngineeringOrchestrator()