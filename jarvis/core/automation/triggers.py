from enum import Enum
from typing import Callable, Dict, Any

class TriggerType(Enum):
    TIME_BASED = "time_based"
    EVENT_BASED = "event_based"
    CONDITION_BASED = "condition_based"

class Trigger:
    def __init__(self, trigger_id: str, trigger_type: TriggerType, condition: Callable, action: Callable):
        self.trigger_id = trigger_id
        self.trigger_type = trigger_type
        self.condition = condition
        self.action = action
        self.is_active = True
        self.execution_count = 0
    
    async def evaluate(self, context: Dict[str, Any]) -> bool:
        try:
            return self.condition(context)
        except:
            return False
    
    async def execute(self, context: Dict[str, Any]):
        if self.is_active:
            try:
                await self.action(context)
                self.execution_count += 1
                return True
            except:
                return False
        return False

class TriggerManager:
    def __init__(self):
        self.triggers = {}
    
    def register_trigger(self, trigger: Trigger):
        self.triggers[trigger.trigger_id] = trigger
    
    async def evaluate_all(self, context: Dict[str, Any]):
        for trigger in self.triggers.values():
            if await trigger.evaluate(context):
                await trigger.execute(context)
    
    def get_trigger_stats(self) -> Dict:
        return {"total_triggers": len(self.triggers)}

_trigger_manager = None

def get_trigger_manager() -> TriggerManager:
    global _trigger_manager
    if _trigger_manager is None:
        _trigger_manager = TriggerManager()
    return _trigger_manager
