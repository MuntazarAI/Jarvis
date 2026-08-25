from typing import List

class LoadBalancer:
    def __init__(self, servers: List[str]):
        self.servers = servers
        self.current = 0
    
    def get_next(self) -> str:
        if not self.servers:
            return None
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server
    
    def add_server(self, server: str):
        if server not in self.servers:
            self.servers.append(server)
    
    def remove_server(self, server: str):
        if server in self.servers:
            self.servers.remove(server)
    
    def get_servers(self) -> List[str]:
        return self.servers.copy()

_balancer = None

def get_load_balancer(servers: List[str] = None):
    global _balancer
    if _balancer is None:
        _balancer = LoadBalancer(servers or [])
    return _balancer
