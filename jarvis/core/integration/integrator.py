from typing import Dict, Callable

class Integration:
    def __init__(self, name: str, service_type: str):
        self.name = name
        self.service_type = service_type
        self.connected = False
        self.config = {}
    
    def connect(self, config: Dict) -> bool:
        self.config = config
        self.connected = True
        return True
    
    def disconnect(self) -> bool:
        self.connected = False
        return True
    
    def is_connected(self) -> bool:
        return self.connected

class IntegrationManager:
    def __init__(self):
        self.integrations = {}
    
    def register_integration(self, name: str, service_type: str) -> Integration:
        integration = Integration(name, service_type)
        self.integrations[name] = integration
        return integration
    
    def get_integration(self, name: str) -> Integration:
        return self.integrations.get(name)
    
    def list_integrations(self) -> Dict:
        return {name: i.service_type for name, i in self.integrations.items()}
    
    def get_connected_integrations(self) -> list:
        return [name for name, i in self.integrations.items() if i.is_connected()]

_manager = None

def get_integration_manager():
    global _manager
    if _manager is None:
        _manager = IntegrationManager()
    return _manager
