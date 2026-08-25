from datetime import datetime, timezone

class AuditLogger:
    def __init__(self):
        self.trail = []
    
    async def log(self, event_type, user_id, agent, action, result):
        self.trail.append({"event": event_type, "user": user_id, "agent": agent, "action": action, "result": result, "time": datetime.now(timezone.utc).isoformat()})
        if len(self.trail) > 10000:
            self.trail = self.trail[-10000:]
    
    def get_trail(self, limit=100):
        return self.trail[-limit:]

_al = None
def get_audit_logger():
    global _al
    if _al is None:
        _al = AuditLogger()
    return _al
