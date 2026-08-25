import pytest
from jarvis.core.automation.triggers import Trigger, TriggerType, TriggerManager

@pytest.fixture
def manager():
    return TriggerManager()

@pytest.mark.asyncio
async def test_trigger_condition(manager):
    results = []
    async def action(ctx):
        results.append(1)
    trigger = Trigger("t1", TriggerType.CONDITION_BASED, lambda c: c.get("val") > 10, action)
    manager.register_trigger(trigger)
    await manager.evaluate_all({"val": 15})
    assert len(results) == 1

@pytest.mark.asyncio
async def test_trigger_no_match(manager):
    results = []
    async def action(ctx):
        results.append(1)
    trigger = Trigger("t1", TriggerType.CONDITION_BASED, lambda c: c.get("val") > 50, action)
    manager.register_trigger(trigger)
    await manager.evaluate_all({"val": 5})
    assert len(results) == 0

def test_trigger_stats(manager):
    trigger = Trigger("t1", TriggerType.TIME_BASED, lambda c: True, lambda c: None)
    manager.register_trigger(trigger)
    stats = manager.get_trigger_stats()
    assert stats["total_triggers"] == 1
