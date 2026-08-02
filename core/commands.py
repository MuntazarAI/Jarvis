"""
commands.py

Executes commands chosen by the planner.
"""

from core.tools import tool_manager

HELP_TEXT = (
    "Jarvis can help with the following commands:\n"
    "- Type or say a question to get an AI response.\n"
    "- Use 'help', 'commands', or 'usage' to see this message again.\n"
    "- Use 'remember' to store important details.\n"
    "- Use 'forget' to remove remembered details in future versions.\n"
    "- Use words like 'search', 'google', or 'find' to search the web.\n"
    "- Use words like 'open', 'launch', or 'start' to open applications.\n"
    "- Type 'exit' or 'quit' to close Jarvis.\n"
    "- Configuration is available in config/defaults.json.\n"
)


def execute(plan):
    """
    Executes planner actions.

    Returns:
        None if the request should continue to the LLM.
        A string if the command has already been handled.
    """

    # --------------------------
    # HELP
    # --------------------------

    if plan.intent == "help":
        return HELP_TEXT

    # --------------------------
    # MEMORY
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
