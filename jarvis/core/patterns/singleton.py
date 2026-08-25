

class Singleton:
    _instances = {}
    
    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class Factory:
    def __init__(self):
        self.creators = {}
    
    def register(self, name: str, creator):
        self.creators[name] = creator
    
    def create(self, name: str, **kwargs):
        if name in self.creators:
            return self.creators[name](**kwargs)
        return None
    
    def list_creators(self) -> list:
        return list(self.creators.keys())
