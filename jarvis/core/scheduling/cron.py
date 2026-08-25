import time
from typing import Callable

class CronJob:
    def __init__(self, job_id: str, cron: str, task: Callable):
        self.job_id = job_id
        self.cron = cron
        self.task = task
        self.last_run = None
        self.runs = 0
    
    async def run(self):
        self.last_run = time.time()
        self.runs += 1
        if hasattr(self.task, '__await__'):
            return await self.task()
        else:
            return self.task()

class CronScheduler:
    def __init__(self):
        self.jobs = {}
    
    def add_job(self, job_id: str, cron: str, task: Callable):
        self.jobs[job_id] = CronJob(job_id, cron, task)
    
    def remove_job(self, job_id: str) -> bool:
        if job_id in self.jobs:
            del self.jobs[job_id]
            return True
        return False
    
    async def run_job(self, job_id: str):
        if job_id in self.jobs:
            return await self.jobs[job_id].run()
        return None
    
    def get_job_info(self, job_id: str) -> dict:
        if job_id in self.jobs:
            job = self.jobs[job_id]
            return {"id": job.job_id, "runs": job.runs, "last_run": job.last_run}
        return {}

_scheduler = None

def get_cron_scheduler():
    global _scheduler
    if _scheduler is None:
        _scheduler = CronScheduler()
    return _scheduler
