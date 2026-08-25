from typing import Dict, Callable

class Container:
    def __init__(self):
        self.services = {}
        self.singletons = {}
    
    def register(self, name: str, factory: Callable):
        self.services[name] = factory
    
    def get(self, name: str):
        if name in self.singletons:
            return self.singletons[name]
        
        if name in self.services:
            instance = self.services[name]()
            self.singletons[name] = instance
            return instance
        return None
    
    def has(self, name: str) -> bool:
        return name in self.services
    
    def list_services(self) -> list:
        return list(self.services.keys())

_container = None

def get_di_container():
    global _container
    if _container is None:
        _container = Container()
    return _container
