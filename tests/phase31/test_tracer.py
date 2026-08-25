import pytest
from jarvis.core.observability.tracer import Tracer

def test_start_span():
    tracer = Tracer()
    span = tracer.start_span("s1", "request")
    assert span.span_id == "s1"

def test_end_span():
    tracer = Tracer()
    span = tracer.start_span("s2", "process")
    span.end()
    assert span.duration > 0

def test_trace_summary():
    tracer = Tracer()
    span = tracer.start_span("s3", "op")
    span.end()
    summary = tracer.get_trace_summary()
    assert summary["total_spans"] > 0
