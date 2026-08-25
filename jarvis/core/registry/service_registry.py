from typing import Dict

class Service:
    def __init__(self, name: str, version: str, url: str):
        self.name = name
        self.version = version
        self.url = url
        self.healthy = True

class ServiceRegistry:
    def __init__(self):
        self.services = {}
    
    def register(self, name: str, version: str, url: str):
        self.services[name] = Service(name, version, url)
    
    def deregister(self, name: str):
        if name in self.services:
            del self.services[name]
    
    def lookup(self, name: str) -> Service:
        return self.services.get(name)
    
    def list_services(self) -> list:
        return [s.name for s in self.services.values()]

_registry = None

def get_service_registry():
    global _registry
    if _registry is None:
        _registry = ServiceRegistry()
    return _registry
