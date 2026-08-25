from analysis.project_scanner import project_scanner
from analysis.dependency_graph import dependency_graph
from analysis.affected_files import affected_files


class EngineeringAnalyzer:
    """
    Builds the engineering context.

    This stage performs only static analysis.
    No AI calls.
    No code generation.
    """

    def analyze(self, context):

        root = context.request.root

        print("[Analyzer] Scanning project...")

        context.project = project_scanner.scan(root)

        print("[Analyzer] Building dependency graph...")

        context.dependency_graph = dependency_graph.build(root)

        print("[Analyzer] Building affected-file graph...")

        context.affected_files = affected_files.build(root)

        return context


engineering_analyzer = EngineeringAnalyzer()