import pytest
from jarvis.core.security.manager import get_security_manager, SecurityDecision

@pytest.fixture
def security_manager():
    return get_security_manager()

@pytest.mark.asyncio
async def test_valid_request(security_manager):
    decision, reason, details = await security_manager.validate_request("Analyze code", "user_1", "reasoning")
    assert decision == SecurityDecision.APPROVED

@pytest.mark.asyncio
async def test_empty_task_denied(security_manager):
    decision, reason, details = await security_manager.validate_request("", "user_1", "reasoning")
    assert decision == SecurityDecision.DENIED

@pytest.mark.asyncio
async def test_injection_detected(security_manager):
    decision, reason, details = await security_manager.validate_request("'; DROP TABLE users;", "user_1", "reasoning")
    assert decision == SecurityDecision.DENIED

def test_security_stats(security_manager):
    stats = security_manager.get_security_stats()
    assert "threat_level" in stats
