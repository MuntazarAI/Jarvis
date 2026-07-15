"""
commands.py

Executes commands chosen by the planner.

Returns:
    None -> continue to the LLM
    str  -> command already handled
"""

from core.browser import google_search
from core.system import open_application


def execute(plan):
    """
    Execute a planner action.

    Parameters
    ----------
    plan : Plan

    Returns
    -------
    str | None
    """

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
    # SYSTEM
    # --------------------------

    if plan.intent == "system":
        return open_application(plan.target)

    # --------------------------
    # BROWSER
    # --------------------------

    if plan.intent == "browser":
        return google_search(plan.target)

    # --------------------------
    # CHAT
    # --------------------------

    return None
