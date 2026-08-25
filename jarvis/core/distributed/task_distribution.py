from typing import List, Dict
import time

class DistributedTask:
    def __init__(self, task_id: str, task_type: str, data: Dict):
        self.task_id = task_id
        self.task_type = task_type
        self.data = data
        self.status = "pending"
        self.assigned_to = None
        self.created_at = time.time()
        self.completed_at = None
    
    def assign_to_node(self, node_id: str):
        """Assign task to node"""
        self.assigned_to = node_id
        self.status = "assigned"
    
    def mark_complete(self, result: Dict):
        """Mark task as complete"""
        self.status = "completed"
        self.completed_at = time.time()
        self.result = result

class TaskDistributor:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.tasks = {}
        self.distribution_history = []
    
    def submit_task(self, task_id: str, task_type: str, data: Dict) -> DistributedTask:
        """Submit task for distribution"""
        task = DistributedTask(task_id, task_type, data)
        self.tasks[task_id] = task
        return task
    
    def distribute_task(self, task_id: str) -> bool:
        """Distribute task to available node"""
        if task_id not in self.tasks:
            return False
        
        task = self.tasks[task_id]
        active_nodes = self.node_manager.get_active_nodes()
        
        if not active_nodes:
            return False
        
        node = active_nodes[0]
        task.assign_to_node(node.node_id)
        node.add_task(task_id, task.data)
        self.distribution_history.append({"task_id": task_id, "node_id": node.node_id, "time": time.time()})
        return True
    
    def get_task_status(self, task_id: str) -> Dict:
        if task_id in self.tasks:
            t = self.tasks[task_id]
            return {"id": t.task_id, "status": t.status, "assigned_to": t.assigned_to}
        return {}
    
    def get_distribution_stats(self) -> Dict:
        completed = sum(1 for t in self.tasks.values() if t.status == "completed")
        return {"total_tasks": len(self.tasks), "completed": completed}

_distributor = None

def get_task_distributor(node_manager):
    global _distributor
    if _distributor is None:
        _distributor = TaskDistributor(node_manager)
    return _distributor
