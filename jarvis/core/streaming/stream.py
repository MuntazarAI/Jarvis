from typing import Callable, List

class Stream:
    def __init__(self, name: str):
        self.name = name
        self.items = []
        self.subscribers = []
    
    def publish(self, item):
        self.items.append(item)
        for sub in self.subscribers:
            sub(item)
    
    def subscribe(self, handler: Callable):
        self.subscribers.append(handler)
    
    def get_items(self) -> List:
        return self.items.copy()

class StreamManager:
    def __init__(self):
        self.streams = {}
    
    def create_stream(self, name: str) -> Stream:
        stream = Stream(name)
        self.streams[name] = stream
        return stream
    
    def get_stream(self, name: str) -> Stream:
        return self.streams.get(name)
    
    def publish(self, stream_name: str, item):
        if stream_name in self.streams:
            self.streams[stream_name].publish(item)
    
    def list_streams(self) -> list:
        return list(self.streams.keys())

_manager = None

def get_stream_manager():
    global _manager
    if _manager is None:
        _manager = StreamManager()
    return _manager
