from typing import Callable, Dict
import time
from enum import Enum

class ScheduleType(Enum):
    ONCE = "once"
    RECURRING = "recurring"

class ScheduledTask:
    def __init__(self, task_id: str, task: Callable, schedule_type: ScheduleType, interval: int = None):
        self.task_id = task_id
        self.task = task
        self.schedule_type = schedule_type
        self.interval = interval
        self.last_executed = None
        self.next_execution = time.time()
        self.execution_count = 0
        self.is_active = True
    
    def is_due(self) -> bool:
        return time.time() >= self.next_execution and self.is_active
    
    async def execute(self):
        if self.is_due():
            try:
                result = await self.task() if hasattr(self.task, '__await__') else self.task()
                self.last_executed = time.time()
                self.execution_count += 1
                if self.schedule_type == ScheduleType.RECURRING and self.interval:
                    self.next_execution = time.time() + self.interval
                return {"status": "success"}
            except Exception as e:
                return {"status": "failed", "error": str(e)}
        return {"status": "pending"}

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
    
    def schedule_task(self, task: ScheduledTask):
        self.tasks[task.task_id] = task
    
    async def run_due_tasks(self):
        for task in self.tasks.values():
            await task.execute()
    
    def get_task_status(self, task_id: str) -> Dict:
        if task_id in self.tasks:
            t = self.tasks[task_id]
            return {"task_id": t.task_id, "executions": t.execution_count, "active": t.is_active}
        return {}

_scheduler = None

def get_task_scheduler() -> TaskScheduler:
    global _scheduler
    if _scheduler is None:
        _scheduler = TaskScheduler()
    return _scheduler
