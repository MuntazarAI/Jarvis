import pytest
from jarvis.core.async_utils.task_manager import AsyncTaskManager

@pytest.mark.asyncio
async def test_create_task():
    manager = AsyncTaskManager()
    async def coro():
        return 42
    task = manager.create_task("t1", coro())
    result = await manager.run_task("t1")
    assert result == 42
