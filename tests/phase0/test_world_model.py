import pytest
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
