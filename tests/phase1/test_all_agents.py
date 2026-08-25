import pytest
from jarvis.core.agents.reasoning_agent import ReasoningAgent
from jarvis.core.agents.coding_agent import CodingAgent
from jarvis.core.agents.research_agent import ResearchAgent
from jarvis.core.agents.vision_agent import VisionAgent
from jarvis.core.agents.system_agent import SystemAgent
from jarvis.core.agents.security_agent import SecurityAgent
from jarvis.core.agents.verification_agent import VerificationAgent

@pytest.mark.asyncio
async def test_reasoning(): 
    assert (await ReasoningAgent().execute("test")).success

@pytest.mark.asyncio
async def test_coding(): 
    assert (await CodingAgent().execute("test")).success

@pytest.mark.asyncio
async def test_research(): 
    assert (await ResearchAgent().execute("test")).success

@pytest.mark.asyncio
async def test_vision(): 
    assert (await VisionAgent().execute("test")).success

@pytest.mark.asyncio
async def test_system(): 
    assert (await SystemAgent().execute("test")).success

@pytest.mark.asyncio
async def test_system_blocked(): 
    assert not (await SystemAgent().execute("rm -rf /")).success

@pytest.mark.asyncio
async def test_security(): 
    assert (await SecurityAgent().execute("test")).success

@pytest.mark.asyncio
async def test_verification(): 
    assert (await VerificationAgent().execute("test")).success
