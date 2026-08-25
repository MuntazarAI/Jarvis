from typing import Dict
import time

class StateSync:
    def __init__(self):
        self.global_state = {}
        self.sync_history = []
        self.version = 0
    
    def sync_state(self, node_id: str, local_state: Dict) -> Dict:
        """Synchronize state between nodes"""
        merged_state = {**self.global_state, **local_state}
        self.global_state = merged_state
        self.version += 1
        self.sync_history.append({"node": node_id, "timestamp": time.time(), "version": self.version})
        return merged_state
    
    def get_state(self) -> Dict:
        """Get current global state"""
        return self.global_state.copy()
    
    def get_version(self) -> int:
        """Get current version"""
        return self.version
    
    def resolve_conflict(self, state1: Dict, state2: Dict, strategy: str = "latest") -> Dict:
        """Resolve conflicts between states"""
        if strategy == "latest":
            return {**state1, **state2}
        elif strategy == "merge":
            result = state1.copy()
            for k, v in state2.items():
                if k not in result:
                    result[k] = v
            return result
        return state1
    
    def get_sync_stats(self) -> Dict:
        return {"total_syncs": len(self.sync_history), "version": self.version}

_sync = None

def get_state_sync():
    global _sync
    if _sync is None:
        _sync = StateSync()
    return _sync
