import time
from typing import Dict

class Deployment:
    def __init__(self, version: str, config: Dict):
        self.version = version
        self.config = config
        self.deployed_at = time.time()
        self.status = "deployed"
    
    def rollback(self):
        self.status = "rolled_back"

class DeploymentManager:
    def __init__(self):
        self.deployments = {}
        self.current_version = None
    
    def deploy(self, version: str, config: Dict) -> bool:
        self.deployments[version] = Deployment(version, config)
        self.current_version = version
        return True
    
    def rollback(self, version: str) -> bool:
        if version in self.deployments:
            self.deployments[version].rollback()
            return True
        return False
    
    def get_current_version(self) -> str:
        return self.current_version
    
    def get_deployment_history(self) -> Dict:
        return {v: d.status for v, d in self.deployments.items()}

_manager = None

def get_deployment_manager():
    global _manager
    if _manager is None:
        _manager = DeploymentManager()
    return _manager
