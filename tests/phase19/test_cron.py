import pytest
from jarvis.core.scheduling.cron import get_cron_scheduler

@pytest.fixture
def scheduler():
    return get_cron_scheduler()

@pytest.mark.asyncio
async def test_add_job(scheduler):
    async def task():
        return "done"
    scheduler.add_job("j1", "*/5 * * * *", task)
    assert "j1" in scheduler.jobs

@pytest.mark.asyncio
async def test_run_job(scheduler):
    def task():
        return 42
    scheduler.add_job("j2", "* * * * *", task)
    result = await scheduler.run_job("j2")
    assert result == 42

def test_remove_job(scheduler):
    def task():
        pass
    scheduler.add_job("j3", "* * * * *", task)
    assert scheduler.remove_job("j3")
