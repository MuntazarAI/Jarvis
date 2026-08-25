from enum import Enum
from typing import List, Dict
import time

class WorkflowState(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class WorkflowStep:
    def __init__(self, step_id: str, agent_type: str, task: str, dependencies: List[str] = None):
        self.step_id = step_id
        self.agent_type = agent_type
        self.task = task
        self.dependencies = dependencies or []
        self.status = WorkflowState.PENDING
        self.result = None

class Workflow:
    def __init__(self, workflow_id: str, name: str, steps: List[WorkflowStep]):
        self.workflow_id = workflow_id
        self.name = name
        self.steps = {step.step_id: step for step in steps}
        self.status = WorkflowState.PENDING
        self.created_at = time.time()
    
    def get_ready_steps(self) -> List[WorkflowStep]:
        ready = []
        for step in self.steps.values():
            if step.status == WorkflowState.PENDING:
                deps_met = all(self.steps[dep].status == WorkflowState.COMPLETED for dep in step.dependencies)
                if deps_met:
                    ready.append(step)
        return ready
    
    def mark_step_complete(self, step_id: str, result):
        if step_id in self.steps:
            self.steps[step_id].status = WorkflowState.COMPLETED
            self.steps[step_id].result = result
    
    def is_complete(self) -> bool:
        return all(s.status in [WorkflowState.COMPLETED, WorkflowState.FAILED] for s in self.steps.values())
    
    def get_status_summary(self) -> Dict:
        completed = sum(1 for s in self.steps.values() if s.status == WorkflowState.COMPLETED)
        return {"workflow_id": self.workflow_id, "name": self.name, "total_steps": len(self.steps), "completed": completed}

class WorkflowEngine:
    def __init__(self):
        self.workflows = {}
    
    def create_workflow(self, workflow_id: str, name: str, steps: List[WorkflowStep]) -> Workflow:
        workflow = Workflow(workflow_id, name, steps)
        self.workflows[workflow_id] = workflow
        return workflow
    
    def get_workflow(self, workflow_id: str) -> Workflow:
        return self.workflows.get(workflow_id)
    
    def list_workflows(self) -> List[Dict]:
        return [w.get_status_summary() for w in self.workflows.values()]

_workflow_engine = None

def get_workflow_engine() -> WorkflowEngine:
    global _workflow_engine
    if _workflow_engine is None:
        _workflow_engine = WorkflowEngine()
    return _workflow_engine
