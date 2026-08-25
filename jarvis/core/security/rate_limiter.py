from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self):
        self.reqs = {}
    
    async def check(self, user_id):
        if user_id not in self.reqs:
            self.reqs[user_id] = []
        now = datetime.now()
        self.reqs[user_id] = [r for r in self.reqs[user_id] if r > (now - timedelta(hours=1))]
        count = sum(1 for r in self.reqs[user_id] if r > (now - timedelta(minutes=1)))
        if count >= 100:
            return False, "Limited"
        self.reqs[user_id].append(now)
        return True, "OK"

_rl = None
def get_rate_limiter():
    global _rl
    if _rl is None:
        _rl = RateLimiter()
    return _rl
