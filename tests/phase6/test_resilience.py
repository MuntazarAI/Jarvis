import pytest
from jarvis.core.distributed.resilience import CircuitBreaker, HealthCheck

@pytest.mark.asyncio
async def test_circuit_breaker():
    cb = CircuitBreaker()
    
    async def test_func():
        return "ok"
    
    result = await cb.call(test_func)
    assert result["status"] == "success"

@pytest.mark.asyncio
async def test_circuit_breaker_failure():
    cb = CircuitBreaker(failure_threshold=2)
    
    async def failing_func():
        raise Exception("fail")
    
    await cb.call(failing_func)
    await cb.call(failing_func)
    assert cb.is_open == True

def test_health_check():
    hc = HealthCheck()
    
    def check():
        return True
    
    hc.register_check("test", check)
    import asyncio
    asyncio.run(hc.run_checks())
    status = hc.get_health_status()
    assert status["status"] == "healthy"
