import time
from typing import Dict

class MetricsCollector:
    def __init__(self):
        self.metrics = {}
        self.timestamps = {}
    
    def record_metric(self, name: str, value: float):
        if name not in self.metrics:
            self.metrics[name] = []
        self.metrics[name].append(value)
        self.timestamps[name] = time.time()
    
    def get_metric(self, name: str) -> Dict:
        if name not in self.metrics:
            return {}
        values = self.metrics[name]
        return {
            "name": name,
            "count": len(values),
            "latest": values[-1],
            "avg": sum(values) / len(values),
            "max": max(values),
            "min": min(values)
        }
    
    def get_all_metrics(self) -> Dict:
        return {name: self.get_metric(name) for name in self.metrics.keys()}

_collector = None

def get_metrics_collector():
    global _collector
    if _collector is None:
        _collector = MetricsCollector()
    return _collector
