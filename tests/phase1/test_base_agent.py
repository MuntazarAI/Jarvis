import pytest
from jarvis.core.agents.base_agent import BaseAgent, AgentType, AgentResult

def test_agent_initialization():
    agent = BaseAgent(AgentType.REASONING)
    assert agent.agent_type == AgentType.REASONING
    assert agent.stats["executed"] == 0

@pytest.mark.asyncio
async def test_track_result():
    agent = BaseAgent(AgentType.CODING)
    result = AgentResult(True, AgentType.CODING, "success", execution_time_ms=100)
    await agent._track_result(result)
    stats = agent.get_stats()
    assert stats["executed"] == 1
    assert stats["successful"] == 1
