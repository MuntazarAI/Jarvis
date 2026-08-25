import time
from typing import Dict

class Logger:
    def __init__(self, name: str):
        self.name = name
        self.logs = []
    
    def log(self, level: str, message: str, metadata: Dict = None):
        entry = {
            "timestamp": time.time(),
            "level": level,
            "message": message,
            "metadata": metadata or {}
        }
        self.logs.append(entry)
    
    def debug(self, msg: str, meta=None):
        self.log("DEBUG", msg, meta)
    
    def info(self, msg: str, meta=None):
        self.log("INFO", msg, meta)
    
    def error(self, msg: str, meta=None):
        self.log("ERROR", msg, meta)
    
    def get_logs(self, level: str = None) -> list:
        if level:
            return [l for l in self.logs if l["level"] == level]
        return self.logs

_loggers = {}

def get_logger(name: str):
    if name not in _loggers:
        _loggers[name] = Logger(name)
    return _loggers[name]
