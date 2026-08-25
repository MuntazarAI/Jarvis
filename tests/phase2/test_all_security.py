import pytest
from jarvis.core.security.permissions import get_permission_manager, Permission
from jarvis.core.security.threat_detector import get_threat_detector
from jarvis.core.security.audit_logger import get_audit_logger
from jarvis.core.security.rate_limiter import get_rate_limiter

def test_permissions():
    pm = get_permission_manager()
    pm.grant("a1", Permission.NETWORK_ACCESS)
    assert pm.check("a1", Permission.NETWORK_ACCESS)

@pytest.mark.asyncio
async def test_threat_sql():
    td = get_threat_detector()
    assert (await td.analyze("'; DROP"))["threat"]

@pytest.mark.asyncio
async def test_threat_clean():
    td = get_threat_detector()
    assert not (await td.analyze("clean"))["threat"]

@pytest.mark.asyncio
async def test_audit():
    al = get_audit_logger()
    await al.log("TEST", "u1", "a1", "act", "ok")
    assert len(al.get_trail()) > 0

@pytest.mark.asyncio
async def test_rate():
    rl = get_rate_limiter()
    ok, _ = await rl.check("u1")
    assert ok
