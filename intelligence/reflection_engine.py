class ReflectionEngine:
    """
    Reviews the last engineering iteration and decides whether
    another iteration is required.
    """

    def reflect(self, context):
        validation = getattr(context, "validation", {}) or {}

        retry = False
        reason = "Task completed."

        if getattr(context, "error", None):
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

        iteration = getattr(context, "iteration", None)
        if iteration is None:
            iteration = len(getattr(context, "history", [])) + 1

        errors = 0
        if hasattr(context, "errors"):
            errors = len(getattr(context, "errors", []))

        reflection = {
            "retry": retry,
            "reason": reason,
            "iteration": iteration,
            "history": len(getattr(context, "history", [])),
            "errors": errors,
            "patches": len(getattr(context, "patches", [])),
        }

        context.analysis["reflection"] = reflection

        if hasattr(context, "memory"):
            try:
                context.memory.remember("reflection", reflection)
            except Exception:
                pass

        return context

    def reply(self, request, result):
        if isinstance(result, dict):
            if result.get("success") is False:
                message = result.get("error") or result.get("stderr") or str(result)
                return f"Execution failed: {message}"

            if "stdout" in result and result["stdout"] is not None:
                return str(result["stdout"]).strip() or "Execution completed successfully."

            if "result" in result:
                return str(result["result"])

            if result.get("tool") and "result" in result:
                return str(result["result"])

            return "Execution completed successfully."

        if isinstance(result, list):
            return "\n".join(str(item) for item in result)

        return str(result)


reflection_engine = ReflectionEngine()

# Backward compatibility
reflection = reflection_engine
