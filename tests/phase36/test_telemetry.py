import pytest
from jarvis.core.telemetry.collector import TelemetryCollector

def test_create_metric():
    collector = TelemetryCollector()
    metric = collector.create_metric("cpu_usage")
    assert "cpu_usage" in collector.metrics

def test_record():
    collector = TelemetryCollector()
    collector.record("memory", 512)
    data = collector.get_metric("memory")
    assert len(data) > 0

def test_add_point():
    collector = TelemetryCollector()
    metric = collector.create_metric("temp")
    metric.add_point(72.5)
    assert len(metric.get_data()) > 0
