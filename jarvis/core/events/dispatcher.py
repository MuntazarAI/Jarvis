from typing import Callable, Dict

class Event:
    def __init__(self, event_type: str, data: Dict = None):
        self.event_type = event_type
        self.data = data or {}
        self.handlers = []
    
    def subscribe(self, handler: Callable):
        self.handlers.append(handler)
    
    async def emit(self):
        for handler in self.handlers:
            if hasattr(handler, '__await__'):
                await handler(self)
            else:
                handler(self)

class EventDispatcher:
    def __init__(self):
        self.events = {}
    
    def register_event(self, event_type: str):
        if event_type not in self.events:
            self.events[event_type] = Event(event_type)
        return self.events[event_type]
    
    def subscribe(self, event_type: str, handler: Callable):
        event = self.register_event(event_type)
        event.subscribe(handler)
    
    async def emit(self, event_type: str, data: Dict = None):
        if event_type in self.events:
            self.events[event_type].data = data or {}
            await self.events[event_type].emit()

_dispatcher = None

def get_event_dispatcher():
    global _dispatcher
    if _dispatcher is None:
        _dispatcher = EventDispatcher()
    return _dispatcher
