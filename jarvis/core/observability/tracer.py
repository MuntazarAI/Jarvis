import time
from typing import Dict

class Span:
    def __init__(self, span_id: str, operation: str):
        self.span_id = span_id
        self.operation = operation
        self.start_time = time.time()
        self.end_time = None
        self.duration = 0
    
    def end(self):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time

class Tracer:
    def __init__(self):
        self.spans = []
    
    def start_span(self, span_id: str, operation: str) -> Span:
        span = Span(span_id, operation)
        self.spans.append(span)
        return span
    
    def get_spans(self) -> list:
        return self.spans.copy()
    
    def get_trace_summary(self) -> Dict:
        total_duration = sum(s.duration for s in self.spans)
        return {"total_spans": len(self.spans), "total_duration": total_duration}

_tracer = None

def get_tracer():
    global _tracer
    if _tracer is None:
        _tracer = Tracer()
    return _tracer
