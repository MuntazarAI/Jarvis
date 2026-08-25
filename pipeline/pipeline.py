from pipeline.analyzer import engineering_analyzer
from pipeline.planner import engineering_planner_stage
from pipeline.executor import engineering_executor_stage
from pipeline.validator import engineering_validator_stage


class EngineeringPipeline:
    """
    Complete autonomous engineering pipeline.

    Workflow:

        Request
            ↓
        Analyze
            ↓
        Plan
            ↓
        Execute
            ↓
        Validate

    Future versions may automatically reflect and retry
    when validation fails.
    """

    def run(self, context):

        context = engineering_analyzer.analyze(context)

        context = engineering_planner_stage.plan(context)

        context = engineering_executor_stage.execute(context)

        context = engineering_validator_stage.validate(context)

        return context


engineering_pipeline = EngineeringPipeline()