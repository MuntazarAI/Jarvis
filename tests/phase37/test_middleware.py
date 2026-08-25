import pytest
from jarvis.core.middleware.chain import MiddlewareChain

@pytest.mark.asyncio
async def test_add_middleware():
    chain = MiddlewareChain()
    chain.add("auth", lambda ctx: ctx)
    assert "auth" in chain.get_chain()

@pytest.mark.asyncio
async def test_execute():
    chain = MiddlewareChain()
    chain.add("m1", lambda ctx: {"done": True})
    result = await chain.execute({})
    assert result is not None
