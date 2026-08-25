from typing import Callable, Dict

class WebSocketConnection:
    def __init__(self, conn_id: str):
        self.conn_id = conn_id
        self.is_open = True
        self.messages = []
    
    def send(self, message: Dict):
        if self.is_open:
            self.messages.append(message)
    
    def close(self):
        self.is_open = False
    
    def get_messages(self) -> list:
        return self.messages.copy()

class WebSocketServer:
    def __init__(self):
        self.connections = {}
        self.handlers = {}
    
    def connect(self, conn_id: str) -> WebSocketConnection:
        conn = WebSocketConnection(conn_id)
        self.connections[conn_id] = conn
        return conn
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            self.connections[conn_id].close()
    
    def register_handler(self, event_type: str, handler: Callable):
        self.handlers[event_type] = handler
    
    def broadcast(self, message: Dict):
        for conn in self.connections.values():
            if conn.is_open:
                conn.send(message)

_server = None

def get_websocket_server():
    global _server
    if _server is None:
        _server = WebSocketServer()
    return _server
