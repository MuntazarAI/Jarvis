import pytest
from jarvis.core.decorators.decorators import retry, timeout, cache_result

@retry(max_attempts=2)
def always_works():
    return "success"

def test_retry():
    result = always_works()
    assert result == "success"

@cache_result(ttl=10)
def expensive_func(x):
    return x * 2

def test_cache():
    result1 = expensive_func(5)
    result2 = expensive_func(5)
    assert result1 == result2 == 10
