import pytest
from jarvis.core.performance.profiler import get_profiler

def test_profile():
    profiler = get_profiler()
    
    @profiler.profile
    def test_func():
        return 42
    
    result = test_func()
    assert result == 42

def test_profiler_stats():
    profiler = get_profiler()
    
    @profiler.profile
    def func():
        return 1
    
    func()
    stats = profiler.get_stats()
    assert stats["calls"] > 0
