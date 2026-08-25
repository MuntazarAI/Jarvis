class ReasoningEngine:
    """
    Produces the internal reasoning of the agent.

    Later this module will call your LLM.
    For now it produces deterministic thoughts.
    """

    def reason(self, state):

        if state.current_step == 1:

            return (
                f"My goal is '{state.goal}'. "
                "I should inspect the project before making changes."
            )

        if state.errors:

            return (
                "Previous action failed. "
                "I should gather more information before continuing."
            )

        return (
            "The previous step succeeded. "
            "Continue toward the objective."
        )


reasoning_engine = ReasoningEngine()