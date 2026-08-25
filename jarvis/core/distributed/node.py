import time
import uuid
from typing import Dict, List

class Node:
    def __init__(self, node_id: str = None, node_type: str = "worker"):
        self.node_id = node_id or str(uuid.uuid4())[:8]
        self.node_type = node_type
        self.is_active = True
        self.created_at = time.time()
        self.last_heartbeat = time.time()
        self.state = {}
        self.tasks = []
    
    def send_heartbeat(self):
        """Send heartbeat to indicate node is alive"""
        self.last_heartbeat = time.time()
        return {"node_id": self.node_id, "status": "alive"}
    
    def is_healthy(self, timeout: int = 30) -> bool:
        """Check if node is healthy based on heartbeat"""
        return time.time() - self.last_heartbeat < timeout
    
    def update_state(self, key: str, value):
        """Update local state"""
        self.state[key] = value
    
    def get_state(self) -> Dict:
        """Get current state"""
        return self.state.copy()
    
    def add_task(self, task_id: str, task: Dict):
        """Add task to node"""
        self.tasks.append({"id": task_id, "data": task, "status": "pending"})
    
    def get_tasks(self) -> List:
        return self.tasks.copy()

class NodeManager:
    def __init__(self):
        self.nodes = {}
        self.node_registry = []
    
    def register_node(self, node: Node):
        """Register node"""
        self.nodes[node.node_id] = node
        self.node_registry.append({"id": node.node_id, "type": node.node_type, "joined_at": time.time()})
    
    def get_active_nodes(self) -> List[Node]:
        """Get all active nodes"""
        return [n for n in self.nodes.values() if n.is_healthy()]
    
    def get_node(self, node_id: str) -> Node:
        return self.nodes.get(node_id)
    
    def broadcast_state(self, state: Dict):
        """Broadcast state to all nodes"""
        for node in self.get_active_nodes():
            for key, value in state.items():
                node.update_state(key, value)
    
    def get_cluster_stats(self) -> Dict:
        return {
            "total_nodes": len(self.nodes),
            "active_nodes": len(self.get_active_nodes()),
            "total_tasks": sum(len(n.get_tasks()) for n in self.nodes.values())
        }

_manager = None

def get_node_manager():
    global _manager
    if _manager is None:
        _manager = NodeManager()
    return _manager
