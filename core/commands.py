"""
commands.py

Executes commands chosen by the planner.
"""

from core.tools import tool_manager


def execute(plan):
    """
    Executes planner actions.

    Returns:
        None if the request should continue to the LLM.
        A string if the command has already been handled.
    """

    # --------------------------
    # Memory
    # --------------------------

    if plan.intent == "memory":

        if plan.action == "remember":
            return (
                "I understood that you want me to remember something. "
                "My memory extractor will save the important details."
            )

        if plan.action == "forget":
            return (
                "Forget requests will be supported in a future version."
            )

    # --------------------------
    # System Tool
    # --------------------------

    if plan.intent == "system":

        return tool_manager.execute(
            "system",
            plan.target,
        )

    # --------------------------
    # Browser Tool
    # --------------------------

    if plan.intent == "browser":

        return tool_manager.execute(
            "browser",
            plan.target,
        )

    # --------------------------
    # Chat
    # --------------------------

    return None
