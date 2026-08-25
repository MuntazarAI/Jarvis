import time
from typing import Dict

class RateLimiter:
    def __init__(self, max_requests: int, window: int):
        self.max_requests = max_requests
        self.window = window
        self.requests = {}
    
    def is_allowed(self, client_id: str) -> bool:
        now = time.time()
        if client_id not in self.requests:
            self.requests[client_id] = []
        
        self.requests[client_id] = [t for t in self.requests[client_id] if now - t < self.window]
        
        if len(self.requests[client_id]) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        return False
    
    def get_status(self, client_id: str) -> Dict:
        if client_id not in self.requests:
            return {"remaining": self.max_requests}
        return {"remaining": self.max_requests - len(self.requests[client_id])}

_limiter = None

def get_rate_limiter(max_requests: int = 100, window: int = 60):
    global _limiter
    if _limiter is None:
        _limiter = RateLimiter(max_requests, window)
    return _limiter
