import pytest
from jarvis.core.ratelimiting.limiter import RateLimiter

def test_allow_request():
    limiter = RateLimiter(5, 60)
    assert limiter.is_allowed("client1")

def test_rate_limit_exceeded():
    limiter = RateLimiter(1, 60)
    limiter.is_allowed("client2")
    assert not limiter.is_allowed("client2")

def test_status():
    limiter = RateLimiter(10, 60)
    limiter.is_allowed("client3")
    status = limiter.get_status("client3")
    assert status["remaining"] == 9
