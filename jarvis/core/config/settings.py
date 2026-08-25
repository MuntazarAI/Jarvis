from typing import Dict, Any

class Config:
    def __init__(self):
        self.settings = {
            "debug": False,
            "host": "localhost",
            "port": 8000,
            "workers": 4,
            "timeout": 30
        }
    
    def set(self, key: str, value: Any):
        self.settings[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)
    
    def get_all(self) -> Dict:
        return self.settings.copy()
    
    def update(self, config: Dict):
        self.settings.update(config)
    
    def validate(self) -> bool:
        required = ["host", "port"]
        return all(k in self.settings for k in required)

_config = None

def get_config():
    global _config
    if _config is None:
        _config = Config()
    return _config
