import pytest
from jarvis.core.events.dispatcher import get_event_dispatcher

@pytest.fixture
def dispatcher():
    return get_event_dispatcher()

@pytest.mark.asyncio
async def test_subscribe(dispatcher):
    called = []
    def handler(event):
        called.append(1)
    dispatcher.subscribe("test", handler)
    await dispatcher.emit("test")
    assert len(called) > 0

@pytest.mark.asyncio
async def test_emit_data(dispatcher):
    data_holder = []
    def handler(event):
        data_holder.append(event.data)
    dispatcher.subscribe("test2", handler)
    await dispatcher.emit("test2", {"key": "value"})
    assert len(data_holder) > 0
