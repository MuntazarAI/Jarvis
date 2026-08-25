"""BaseAgent - Base class for agents"""
from typing import Dict, Any
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class AgentType(Enum):
    REASONING = "reasoning"
    CODING = "coding"
    RESEARCH = "research"
    VISION = "vision"
    SYSTEM = "system"
    SECURITY = "security"
    VERIFICATION = "verification"

class AgentResult:
    def __init__(self, success: bool, agent_type: AgentType, result: Any = None, reasoning: str = "", execution_time_ms: float = 0.0, error: str = ""):
        self.success = success
        self.agent_type = agent_type
        self.result = result
        self.reasoning = reasoning
        self.execution_time_ms = execution_time_ms
        self.error = error
        self.timestamp = datetime.now().isoformat()

class BaseAgent:
    def __init__(self, agent_type: AgentType, max_retries: int = 2):
        self.agent_type = agent_type
        self.max_retries = max_retries
        self.stats = {"executed": 0, "successful": 0, "failed": 0, "total_time": 0.0}
        logger.info(f"{agent_type.value} agent initialized")
    
    async def execute(self, task: str, context: Dict[str, Any] = None) -> AgentResult:
        raise NotImplementedError()
    
    async def _track_result(self, result: AgentResult) -> None:
        self.stats["executed"] += 1
        if result.success:
            self.stats["successful"] += 1
        else:
            self.stats["failed"] += 1
        self.stats["total_time"] += result.execution_time_ms
    
    def get_stats(self) -> Dict[str, Any]:
        return self.stats.copy()
