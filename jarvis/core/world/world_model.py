"""WorldModel - System state tracking"""
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
