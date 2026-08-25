"""AgentSupervisor - Route tasks"""
from typing import Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, timeout_seconds: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.failure_count = 0
        self.last_failure_time = None
        self.is_open = False
    
    def record_failure(self) -> None:
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        if self.failure_count >= self.failure_threshold:
            self.is_open = True
    
    def record_success(self) -> None:
        self.failure_count = 0
        self.is_open = False
    
    def is_available(self) -> bool:
        if not self.is_open:
            return True
        if self.last_failure_time and (datetime.now() - self.last_failure_time).total_seconds() > self.timeout_seconds:
            self.is_open = False
            self.failure_count = 0
            return True
        return False

class AgentSupervisor:
    def __init__(self):
        self.agents: Dict[str, Any] = {}
        self.breakers: Dict[str, CircuitBreaker] = {}
        logger.info("AgentSupervisor initialized")
    
    def register_agent(self, agent_type: str, agent: Any) -> None:
        self.agents[agent_type] = agent
        self.breakers[agent_type] = CircuitBreaker()
    
    async def execute_task(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        agent_type = self._route_task(task)
        if agent_type not in self.agents:
            return {"success": False, "error": f"No agent for {agent_type}"}
        breaker = self.breakers[agent_type]
        if not breaker.is_available():
            return {"success": False, "error": f"Agent {agent_type} unavailable"}
        try:
            result = await self.agents[agent_type].execute(task, context)
            breaker.record_success()
            return {"success": result.success, "result": result.result}
        except Exception as e:
            breaker.record_failure()
            return {"success": False, "error": str(e)}
    
    def _route_task(self, task: str) -> str:
        task_lower = task.lower()
        if any(word in task_lower for word in ["code", "python"]):
            return "coding"
        elif any(word in task_lower for word in ["search", "research"]):
            return "research"
        else:
            return "reasoning"
