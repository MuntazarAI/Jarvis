from typing import Dict, Callable
import time
import inspect

class APIEndpoint:
    def __init__(self, path: str, method: str, handler: Callable):
        self.path = path
        self.method = method
        self.handler = handler
        self.calls = 0
    
    async def handle(self, request: Dict):
        self.calls += 1
        if inspect.iscoroutinefunction(self.handler):
            return await self.handler(request)
        else:
            return self.handler(request)

class APIGateway:
    def __init__(self):
        self.routes = {}
        self.middleware = []
    
    def register_route(self, path: str, method: str, handler: Callable):
        key = f"{method}:{path}"
        self.routes[key] = APIEndpoint(path, method, handler)
    
    async def route_request(self, path: str, method: str, request: Dict) -> Dict:
        key = f"{method}:{path}"
        if key in self.routes:
            return await self.routes[key].handle(request)
        return {"error": "Not found", "status": 404}
    
    def add_middleware(self, middleware: Callable):
        self.middleware.append(middleware)
    
    def get_stats(self) -> Dict:
        return {"total_routes": len(self.routes), "total_calls": sum(e.calls for e in self.routes.values())}

_gateway = None

def get_api_gateway():
    global _gateway
    if _gateway is None:
        _gateway = APIGateway()
    return _gateway
