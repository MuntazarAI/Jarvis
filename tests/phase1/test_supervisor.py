import pytest
from jarvis.core.agents.supervisor import AgentSupervisor, CircuitBreaker

def test_circuit_breaker():
    breaker = CircuitBreaker(failure_threshold=2)
    assert breaker.is_available()
    breaker.record_failure()
    assert breaker.is_available()
    breaker.record_failure()
    assert not breaker.is_available()

def test_supervisor_init():
    supervisor = AgentSupervisor()
    assert len(supervisor.agents) == 0

def test_task_routing():
    supervisor = AgentSupervisor()
    assert supervisor._route_task("write some python code") == "coding"
    assert supervisor._route_task("research this topic") == "research"
