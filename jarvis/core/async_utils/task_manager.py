import asyncio
from typing import Callable

class AsyncTask:
    def __init__(self, task_id: str, coro):
        self.task_id = task_id
        self.coro = coro
        self.result = None
        self.done = False
    
    async def run(self):
        self.result = await self.coro
        self.done = True
        return self.result

class AsyncTaskManager:
    def __init__(self):
        self.tasks = {}
    
    def create_task(self, task_id: str, coro):
        task = AsyncTask(task_id, coro)
        self.tasks[task_id] = task
        return task
    
    async def run_task(self, task_id: str):
        if task_id in self.tasks:
            return await self.tasks[task_id].run()
        return None
    
    def get_task_status(self, task_id: str) -> dict:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            return {"done": task.done, "result": task.result}
        return {}
