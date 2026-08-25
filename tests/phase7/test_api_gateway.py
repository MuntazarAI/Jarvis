import pytest
from jarvis.core.api.gateway import get_api_gateway

@pytest.fixture
def gateway():
    return get_api_gateway()

@pytest.mark.asyncio
async def test_register_route(gateway):
    async def handler(req):
        return {"status": "ok"}
    gateway.register_route("/test", "GET", handler)
    assert len(gateway.routes) > 0

@pytest.mark.asyncio
async def test_route_request(gateway):
    async def handler(req):
        return {"result": "success"}
    gateway.register_route("/api/test", "POST", handler)
    result = await gateway.route_request("/api/test", "POST", {})
    assert result["result"] == "success"

def test_gateway_stats(gateway):
    def handler(req):
        return {"ok": True}
    gateway.register_route("/test", "GET", handler)
    stats = gateway.get_stats()
    assert stats["total_routes"] > 0
