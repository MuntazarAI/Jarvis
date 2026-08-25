from enum import Enum
from typing import List, Callable

class ChainType(Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"

class Chain:
    def __init__(self, chain_id: str, chain_type: ChainType, tasks: List[Callable]):
        self.chain_id = chain_id
        self.chain_type = chain_type
        self.tasks = tasks
        self.results = []
        self.status = "pending"
    
    async def execute(self) -> List:
        results = []
        for task in self.tasks:
            try:
                result = await task() if hasattr(task, '__await__') else task()
                results.append({"status": "success", "result": result})
            except Exception as e:
                results.append({"status": "failed", "error": str(e)})
        self.results = results
        self.status = "completed"
        return results
    
    def get_summary(self) -> dict:
        successful = sum(1 for r in self.results if r.get("status") == "success")
        return {"chain_id": self.chain_id, "total_tasks": len(self.tasks), "successful": successful}

class ChainManager:
    def __init__(self):
        self.chains = {}
    
    def register_chain(self, chain: Chain):
        self.chains[chain.chain_id] = chain
    
    async def execute_chain(self, chain_id: str):
        if chain_id in self.chains:
            chain = self.chains[chain_id]
            return await chain.execute()
        return []
    
    def list_chains(self) -> list:
        return [c.get_summary() for c in self.chains.values()]

_chain_manager = None

def get_chain_manager() -> ChainManager:
    global _chain_manager
    if _chain_manager is None:
        _chain_manager = ChainManager()
    return _chain_manager
