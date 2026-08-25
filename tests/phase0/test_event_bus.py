import pytest
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
