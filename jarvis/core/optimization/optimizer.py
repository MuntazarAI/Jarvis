from typing import Dict

class OptimizationMetrics:
    def __init__(self):
        self.metrics = {}
    
    def record_execution(self, operation: str, duration: float):
        if operation not in self.metrics:
            self.metrics[operation] = []
        self.metrics[operation].append(duration)
    
    def get_average(self, operation: str) -> float:
        if operation in self.metrics:
            durations = self.metrics[operation]
            return sum(durations) / len(durations)
        return 0
    
    def get_slowest(self, operation: str) -> float:
        if operation in self.metrics:
            return max(self.metrics[operation])
        return 0
    
    def get_optimization_report(self) -> Dict:
        report = {}
        for op, durations in self.metrics.items():
            report[op] = {
                "calls": len(durations),
                "avg": self.get_average(op),
                "max": self.get_slowest(op)
            }
        return report

_metrics = None

def get_optimization_metrics():
    global _metrics
    if _metrics is None:
        _metrics = OptimizationMetrics()
    return _metrics
