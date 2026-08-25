import time
from typing import Dict

class Cache:
    def __init__(self, ttl: int = 3600):
        self.data = {}
        self.ttl = ttl
        self.timestamps = {}
    
    def set(self, key: str, value):
        self.data[key] = value
        self.timestamps[key] = time.time()
    
    def get(self, key: str):
        if key not in self.data:
            return None
        if time.time() - self.timestamps[key] > self.ttl:
            del self.data[key]
            del self.timestamps[key]
            return None
        return self.data[key]
    
    def delete(self, key: str):
        if key in self.data:
            del self.data[key]
            del self.timestamps[key]
    
    def clear(self):
        self.data.clear()
        self.timestamps.clear()
    
    def get_stats(self) -> Dict:
        return {"size": len(self.data), "ttl": self.ttl}

_cache = None

def get_cache(ttl: int = 3600):
    global _cache
    if _cache is None:
        _cache = Cache(ttl)
    return _cache
