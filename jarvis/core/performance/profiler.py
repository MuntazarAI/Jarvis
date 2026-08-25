import time
from typing import Callable

class ProfileResult:
    def __init__(self, name: str, duration: float):
        self.name = name
        self.duration = duration
        self.timestamp = time.time()

class Profiler:
    def __init__(self):
        self.results = []
    
    def profile(self, func: Callable):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            self.results.append(ProfileResult(func.__name__, duration))
            return result
        return wrapper
    
    async def async_profile(self, func: Callable):
        async def wrapper(*args, **kwargs):
            start = time.time()
            result = await func(*args, **kwargs)
            duration = time.time() - start
            self.results.append(ProfileResult(func.__name__, duration))
            return result
        return wrapper
    
    def get_stats(self) -> dict:
        if not self.results:
            return {}
        durations = [r.duration for r in self.results]
        return {
            "calls": len(self.results),
            "avg": sum(durations) / len(durations),
            "max": max(durations),
            "min": min(durations)
        }

_profiler = None

def get_profiler():
    global _profiler
    if _profiler is None:
        _profiler = Profiler()
    return _profiler
