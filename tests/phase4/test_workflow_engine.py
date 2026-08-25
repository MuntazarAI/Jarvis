import pytest
from jarvis.core.automation.workflow_engine import WorkflowEngine, WorkflowStep

@pytest.fixture
def engine():
    return WorkflowEngine()

def test_create_workflow(engine):
    steps = [WorkflowStep("s1", "reasoning", "task1")]
    workflow = engine.create_workflow("w1", "Test", steps)
    assert workflow.workflow_id == "w1"

def test_get_ready_steps(engine):
    steps = [
        WorkflowStep("s1", "reasoning", "task1"),
        WorkflowStep("s2", "coding", "task2", ["s1"])
    ]
    workflow = engine.create_workflow("w1", "Test", steps)
    ready = workflow.get_ready_steps()
    assert len(ready) == 1

def test_list_workflows(engine):
    steps = [WorkflowStep("s1", "reasoning", "task1")]
    engine.create_workflow("w1", "Test1", steps)
    engine.create_workflow("w2", "Test2", steps)
    workflows = engine.list_workflows()
    assert len(workflows) == 2
