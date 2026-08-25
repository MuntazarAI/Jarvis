import pytest
from jarvis.core.distributed.state_sync import StateSync

@pytest.fixture
def sync():
    return StateSync()

def test_sync_state(sync):
    result = sync.sync_state("n1", {"a": 1})
    assert result["a"] == 1

def test_version_increment(sync):
    sync.sync_state("n1", {"a": 1})
    assert sync.get_version() == 1

def test_resolve_conflict(sync):
    s1 = {"a": 1}
    s2 = {"b": 2}
    result = sync.resolve_conflict(s1, s2)
    assert "a" in result and "b" in result

def test_sync_stats(sync):
    sync.sync_state("n1", {"a": 1})
    stats = sync.get_sync_stats()
    assert stats["total_syncs"] == 1
