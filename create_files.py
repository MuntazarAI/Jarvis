import os

# Create all Python files
files = {
    "jarvis/core/world/event_bus.py": '''"""EventBus - Pub/sub event system"""
from typing import Callable, List, Dict, Any
from enum import Enum
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

class EventType(Enum):
    TOOL_REQUESTED = "tool_requested"
    TOOL_COMPLETED = "tool_completed"
    TOOL_FAILED = "tool_failed"

class BusEvent:
    def __init__(self, event_type: EventType, data: Dict[str, Any]):
        self.event_type = event_type
        self.data = data
        self.timestamp = datetime.now(timezone.utc).isoformat()

class EventBus:
    def __init__(self):
        self.handlers: Dict[EventType, List[Callable]] = {}
        self.history: List[BusEvent] = []
        logger.info("EventBus initialized")
    
    async def publish(self, event: BusEvent) -> None:
        self.history.append(event)
        if len(self.history) > 1000:
            self.history = self.history[-1000:]
        if event.event_type in self.handlers:
            for handler in self.handlers[event.event_type]:
                try:
                    await handler(event)
                except Exception as e:
                    logger.error(f"Handler error: {e}")
    
    def subscribe(self, event_type: EventType, handler: Callable) -> None:
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
    
    def get_history(self, limit: int = 100) -> List[BusEvent]:
        return self.history[-limit:]

_event_bus = None

def get_event_bus() -> EventBus:
    global _event_bus
    if _event_bus is None:
        _event_bus = EventBus()
    return _event_bus
''',
    
    "jarvis/core/world/world_model.py": '''"""WorldModel - System state tracking"""
from typing import Dict, List, Any
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

class WorldModel:
    def __init__(self):
        self.system_state = {"cpu": 0.0, "memory": 0.0, "disk": 0.0, "temperature": 0.0}
        self.tasks: Dict[str, Dict[str, Any]] = {}
        self.observations: List[Dict[str, Any]] = []
        logger.info("WorldModel initialized")
    
    async def update_system_state(self, cpu: float, memory: float, disk: float, temperature: float) -> None:
        self.system_state = {"cpu": cpu, "memory": memory, "disk": disk, "temperature": temperature, "timestamp": datetime.now(timezone.utc).isoformat()}
    
    def create_task(self, task_id: str, task_name: str) -> None:
        self.tasks[task_id] = {"id": task_id, "name": task_name, "status": "created", "created_at": datetime.now(timezone.utc).isoformat()}
    
    def is_system_healthy(self) -> bool:
        return self.system_state["cpu"] < 80 and self.system_state["memory"] < 85

_world_model = None

def get_world_model() -> WorldModel:
    global _world_model
    if _world_model is None:
        _world_model = WorldModel()
    return _world_model
''',
    
    "jarvis/core/agents/base_agent.py": '''"""BaseAgent - Base class for agents"""
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
''',
    
    "jarvis/core/agents/supervisor.py": '''"""AgentSupervisor - Route tasks"""
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
''',
    
    "jarvis/core/security/manager.py": '''"""SecurityManager - Zero-trust validation"""
from typing import Dict, List, Any
from datetime import datetime, timezone
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class ThreatLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SecurityDecision(Enum):
    APPROVED = "approved"
    DENIED = "denied"

class SecurityManager:
    def __init__(self):
        self.threat_level = ThreatLevel.LOW
        self.blocked_count = 0
        self.approved_count = 0
        self.security_events: List[Dict[str, Any]] = []
        logger.info("SecurityManager initialized")
    
    async def validate_request(self, task: str, user_id: str, agent_type: str, context: Dict[str, Any] = None) -> tuple:
        if not task or not isinstance(task, str) or len(task.strip()) == 0:
            self.blocked_count += 1
            return SecurityDecision.DENIED, "Empty task", {}
        if self._check_injection_patterns(task):
            self.threat_level = ThreatLevel.HIGH
            self.blocked_count += 1
            return SecurityDecision.DENIED, "Injection detected", {}
        self.approved_count += 1
        return SecurityDecision.APPROVED, "Approved", {}
    
    def _check_injection_patterns(self, task: str) -> bool:
        patterns = ["'; DROP", "OR 1=1", "__import__", "eval("]
        return any(p.lower() in task.lower() for p in patterns)
    
    def get_security_stats(self) -> Dict[str, Any]:
        total = self.blocked_count + self.approved_count
        return {"threat_level": self.threat_level.value, "blocked": self.blocked_count, "approved": self.approved_count, "total": total}

_security_manager = None

def get_security_manager() -> SecurityManager:
    global _security_manager
    if _security_manager is None:
        _security_manager = SecurityManager()
    return _security_manager
''',

    "tests/phase0/test_event_bus.py": '''import pytest
from jarvis.core.world.event_bus import EventBus, EventType, BusEvent

@pytest.fixture
def event_bus():
    return EventBus()

@pytest.mark.asyncio
async def test_publish_event(event_bus):
    event = BusEvent(EventType.TOOL_REQUESTED, {"tool": "test"})
    await event_bus.publish(event)
    history = event_bus.get_history()
    assert len(history) == 1
    assert history[0].event_type == EventType.TOOL_REQUESTED

@pytest.mark.asyncio
async def test_subscribe_handler(event_bus):
    received = []
    async def handler(event):
        received.append(event)
    event_bus.subscribe(EventType.TOOL_COMPLETED, handler)
    event = BusEvent(EventType.TOOL_COMPLETED, {"result": "done"})
    await event_bus.publish(event)
    assert len(received) == 1

def test_event_history(event_bus):
    assert len(event_bus.get_history()) == 0
''',

    "tests/phase0/test_world_model.py": '''import pytest
from jarvis.core.world.world_model import WorldModel

@pytest.fixture
def world_model():
    return WorldModel()

@pytest.mark.asyncio
async def test_update_system_state(world_model):
    await world_model.update_system_state(50.0, 60.0, 70.0, 45.0)
    assert world_model.system_state["cpu"] == 50.0
    assert world_model.system_state["memory"] == 60.0

def test_system_health(world_model):
    world_model.system_state = {"cpu": 75.0, "memory": 80.0}
    assert world_model.is_system_healthy()
    world_model.system_state = {"cpu": 90.0, "memory": 80.0}
    assert not world_model.is_system_healthy()

def test_task_creation(world_model):
    world_model.create_task("task_1", "test task")
    assert "task_1" in world_model.tasks
    assert world_model.tasks["task_1"]["name"] == "test task"
''',

    "tests/phase1/test_base_agent.py": '''import pytest
from jarvis.core.agents.base_agent import BaseAgent, AgentType, AgentResult

def test_agent_initialization():
    agent = BaseAgent(AgentType.REASONING)
    assert agent.agent_type == AgentType.REASONING
    assert agent.stats["executed"] == 0

@pytest.mark.asyncio
async def test_track_result():
    agent = BaseAgent(AgentType.CODING)
    result = AgentResult(True, AgentType.CODING, "success", execution_time_ms=100)
    await agent._track_result(result)
    stats = agent.get_stats()
    assert stats["executed"] == 1
    assert stats["successful"] == 1
''',

    "tests/phase1/test_supervisor.py": '''import pytest
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
''',

    "tests/phase2/test_security_manager.py": '''import pytest
from jarvis.core.security.manager import get_security_manager, SecurityDecision

@pytest.fixture
def security_manager():
    return get_security_manager()

@pytest.mark.asyncio
async def test_valid_request(security_manager):
    decision, reason, details = await security_manager.validate_request("Analyze code", "user_1", "reasoning")
    assert decision == SecurityDecision.APPROVED

@pytest.mark.asyncio
async def test_empty_task_denied(security_manager):
    decision, reason, details = await security_manager.validate_request("", "user_1", "reasoning")
    assert decision == SecurityDecision.DENIED

@pytest.mark.asyncio
async def test_injection_detected(security_manager):
    decision, reason, details = await security_manager.validate_request("'; DROP TABLE users;", "user_1", "reasoning")
    assert decision == SecurityDecision.DENIED

def test_security_stats(security_manager):
    stats = security_manager.get_security_stats()
    assert "threat_level" in stats
''',

    "pyproject.toml": '''[project]
name = "jarvis"
version = "0.1.0"
description = "JARVIS Ultimate Blueprint"

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
python_files = "test_*.py"
''',
}

# Create all files
for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Created {filepath}")

print("\n✨ All files created!")
