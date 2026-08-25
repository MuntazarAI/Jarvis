from typing import Callable, List

class Middleware:
    def __init__(self, name: str, handler: Callable):
        self.name = name
        self.handler = handler
    
    async def execute(self, context):
        if hasattr(self.handler, '__await__'):
            return await self.handler(context)
        else:
            return self.handler(context)

class MiddlewareChain:
    def __init__(self):
        self.middlewares = []
    
    def add(self, name: str, handler: Callable):
        self.middlewares.append(Middleware(name, handler))
    
    async def execute(self, context):
        for middleware in self.middlewares:
            context = await middleware.execute(context)
        return context
    
    def get_chain(self) -> List[str]:
        return [m.name for m in self.middlewares]

_chain = None

def get_middleware_chain():
    global _chain
    if _chain is None:
        _chain = MiddlewareChain()
    return _chain
