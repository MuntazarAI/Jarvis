import pytest
from jarvis.core.automation.task_scheduler import TaskScheduler, ScheduledTask, ScheduleType

@pytest.fixture
def scheduler():
    return TaskScheduler()

@pytest.mark.asyncio
async def test_schedule_once(scheduler):
    def task():
        return "done"
    st = ScheduledTask("t1", task, ScheduleType.ONCE)
    scheduler.schedule_task(st)
    await scheduler.run_due_tasks()
    assert st.execution_count == 1

@pytest.mark.asyncio
async def test_schedule_recurring(scheduler):
    def task():
        return "done"
    st = ScheduledTask("t1", task, ScheduleType.RECURRING, interval=1)
    scheduler.schedule_task(st)
    await scheduler.run_due_tasks()
    assert st.execution_count == 1

def test_task_status(scheduler):
    def task():
        return "done"
    st = ScheduledTask("t1", task, ScheduleType.ONCE)
    scheduler.schedule_task(st)
    status = scheduler.get_task_status("t1")
    assert status["task_id"] == "t1"
