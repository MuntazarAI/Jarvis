import pytest
from jarvis.core.agents.adaptation_engine import get_adaptation_engine
from jarvis.core.agents.base_agent import AgentResult, AgentType

@pytest.mark.asyncio
async def test_learn():
    engine = get_adaptation_engine()
    result = AgentResult(True, AgentType.REASONING, "test", "", 10.0)
    await engine.learn_from_result("agent1", result)
    stats = engine.get_performance_stats("agent1")
    assert stats["success"] >= 1

@pytest.mark.asyncio
async def test_insights():
    engine = get_adaptation_engine()
    insights = engine.get_learning_insights()
    assert "total_learned" in insights
