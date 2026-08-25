from typing import Dict
import time

class Message:
    def __init__(self, msg_id: str, content: Dict):
        self.msg_id = msg_id
        self.content = content
        self.timestamp = time.time()
        self.consumed = False

class MessageQueue:
    def __init__(self, name: str):
        self.name = name
        self.messages = []
    
    def enqueue(self, msg_id: str, content: Dict) -> Message:
        msg = Message(msg_id, content)
        self.messages.append(msg)
        return msg
    
    def dequeue(self) -> Message:
        if self.messages:
            msg = self.messages.pop(0)
            msg.consumed = True
            return msg
        return None
    
    def size(self) -> int:
        return len([m for m in self.messages if not m.consumed])
    
    def get_stats(self) -> Dict:
        return {"size": self.size(), "total_messages": len(self.messages)}

class QueueManager:
    def __init__(self):
        self.queues = {}
    
    def create_queue(self, name: str) -> MessageQueue:
        queue = MessageQueue(name)
        self.queues[name] = queue
        return queue
    
    def get_queue(self, name: str) -> MessageQueue:
        return self.queues.get(name)
    
    def list_queues(self) -> list:
        return list(self.queues.keys())

_manager = None

def get_queue_manager():
    global _manager
    if _manager is None:
        _manager = QueueManager()
    return _manager
