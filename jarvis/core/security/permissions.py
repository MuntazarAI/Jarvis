from enum import Enum

class Permission(Enum):
    EXECUTE_CODE = "execute_code"
    ACCESS_FILES = "access_files"
    NETWORK_ACCESS = "network_access"

class PermissionManager:
    def __init__(self):
        self.perms = {}
        self.defaults = {Permission.EXECUTE_CODE}
    
    def grant(self, agent, perm):
        if agent not in self.perms:
            self.perms[agent] = set(self.defaults)
        self.perms[agent].add(perm)
    
    def check(self, agent, perm):
        if agent not in self.perms:
            self.perms[agent] = set(self.defaults)
        return perm in self.perms[agent]

_pm = None
def get_permission_manager():
    global _pm
    if _pm is None:
        _pm = PermissionManager()
    return _pm
