from typing import Dict

class Analytics:
    def __init__(self):
        self.events = []
        self.counters = {}
    
    def track_event(self, event_name: str, properties: Dict = None):
        self.events.append({
            "name": event_name,
            "properties": properties or {}
        })
    
    def increment_counter(self, name: str, value: int = 1):
        if name not in self.counters:
            self.counters[name] = 0
        self.counters[name] += value
    
    def get_counter(self, name: str) -> int:
        return self.counters.get(name, 0)
    
    def get_events(self) -> list:
        return self.events.copy()
    
    def get_summary(self) -> Dict:
        return {
            "total_events": len(self.events),
            "counters": self.counters.copy()
        }

_analytics = None

def get_analytics():
    global _analytics
    if _analytics is None:
        _analytics = Analytics()
    return _analytics
