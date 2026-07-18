class ReflectionEngine:
    """
    Reviews the last engineering iteration and decides whether
    another iteration is required.
    """

    def reflect(self, context):

        validation = context.validation

        retry = False
        reason = "Task completed."

        if context.error:
            retry = True
            reason = context.error

        elif validation.get("failed_steps", 0) > 0:
            retry = True
            reason = "Execution failed."

        elif not validation.get("syntax_ok", True):
            retry = True
            reason = "Syntax validation failed."

        elif not validation.get("tests_ok", True):
            retry = True
            reason = "Tests failed."

        reflection = {
            "retry": retry,
            "reason": reason,
            "iteration": context.memory.iteration,
            "history": len(context.memory.history),
            "errors": len(context.memory.errors),
            "patches": len(context.memory.patches),
        }

        context.analysis["reflection"] = reflection

        context.memory.remember(
            "reflection",
            reflection,
        )

        return context

reflection_engine = ReflectionEngine()

# Backward compatibility
reflection = reflection_engine
