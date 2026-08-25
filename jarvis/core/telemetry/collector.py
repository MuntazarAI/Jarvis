import time
from typing import Dict

class Telemetry:
    def __init__(self, metric_name: str):
        self.metric_name = metric_name
        self.data_points = []
    
    def add_point(self, value, timestamp=None):
        self.data_points.append({
            "value": value,
            "timestamp": timestamp or time.time()
        })
    
    def get_data(self) -> list:
        return self.data_points.copy()

class TelemetryCollector:
    def __init__(self):
        self.metrics = {}
    
    def create_metric(self, name: str) -> Telemetry:
        metric = Telemetry(name)
        self.metrics[name] = metric
        return metric
    
    def record(self, metric_name: str, value):
        if metric_name not in self.metrics:
            self.create_metric(metric_name)
        self.metrics[metric_name].add_point(value)
    
    def get_metric(self, name: str) -> list:
        if name in self.metrics:
            return self.metrics[name].get_data()
        return []

_collector = None

def get_telemetry_collector():
    global _collector
    if _collector is None:
        _collector = TelemetryCollector()
    return _collector
