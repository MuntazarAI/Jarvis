from core.planner import Planner
from core.commands import execute


def test_help_planner_recognizes_help_requests():
    planner = Planner()
    plan = planner.create_plan("help")

    assert plan.intent == "help"
    assert plan.action == "help"


def test_help_command_returns_user_friendly_text():
    plan = type("Plan", (), {"intent": "help", "action": "help", "target": "help"})()
    result = execute(plan)

    assert isinstance(result, str)
    assert "help" in result.lower()
    assert "remember" in result.lower()
    assert "search" in result.lower()
