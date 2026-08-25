import pytest
from jarvis.core.optimization.optimizer import OptimizationMetrics

def test_record_execution():
    metrics = OptimizationMetrics()
    metrics.record_execution("query", 0.5)
    assert "query" in metrics.metrics

def test_get_average():
    metrics = OptimizationMetrics()
    metrics.record_execution("op1", 1.0)
    metrics.record_execution("op1", 2.0)
    avg = metrics.get_average("op1")
    assert avg == 1.5

def test_optimization_report():
    metrics = OptimizationMetrics()
    metrics.record_execution("op", 0.1)
    report = metrics.get_optimization_report()
    assert "op" in report
