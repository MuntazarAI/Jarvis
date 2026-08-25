"""EventBus - Pub/sub event system"""
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
