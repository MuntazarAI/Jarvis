import pytest
from jarvis.core.caching.cache import get_cache

@pytest.fixture
def cache():
    return get_cache(ttl=3600)

def test_set_get(cache):
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"

def test_delete(cache):
    cache.set("key1", "value1")
    cache.delete("key1")
    assert cache.get("key1") is None

def test_cache_stats(cache):
    cache.set("k1", "v1")
    stats = cache.get_stats()
    assert stats["size"] > 0
