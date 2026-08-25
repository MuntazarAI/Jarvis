import pytest
from jarvis.core.monitoring.metrics import get_metrics_collector

@pytest.fixture
def collector():
    return get_metrics_collector()

def test_record_metric(collector):
    collector.record_metric("requests", 100)
    metric = collector.get_metric("requests")
    assert metric["latest"] == 100

def test_metric_stats(collector):
    collector.record_metric("latency", 10)
    collector.record_metric("latency", 20)
    metric = collector.get_metric("latency")
    assert metric["avg"] == 15

def test_all_metrics(collector):
    collector.record_metric("m1", 1)
    collector.record_metric("m2", 2)
    all_m = collector.get_all_metrics()
    assert len(all_m) >= 2
