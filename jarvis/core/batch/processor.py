from typing import List, Callable

class Batch:
    def __init__(self, batch_id: str, items: List):
        self.batch_id = batch_id
        self.items = items
        self.results = []
    
    async def process(self, func: Callable):
        for item in self.items:
            result = await func(item) if hasattr(func, '__await__') else func(item)
            self.results.append(result)
        return self.results

class BatchProcessor:
    def __init__(self, batch_size: int = 10):
        self.batch_size = batch_size
        self.batches = {}
    
    def create_batch(self, batch_id: str, items: List) -> Batch:
        batch = Batch(batch_id, items)
        self.batches[batch_id] = batch
        return batch
    
    async def process_batch(self, batch_id: str, func: Callable):
        if batch_id in self.batches:
            return await self.batches[batch_id].process(func)
        return []
