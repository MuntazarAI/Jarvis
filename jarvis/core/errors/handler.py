from typing import Dict, Callable

class ErrorHandler:
    def __init__(self):
        self.handlers = {}
        self.error_log = []
    
    def register_handler(self, error_type: str, handler: Callable):
        self.handlers[error_type] = handler
    
    def handle(self, error_type: str, error: Exception) -> Dict:
        self.error_log.append({"type": error_type, "message": str(error)})
        if error_type in self.handlers:
            return self.handlers[error_type](error)
        return {"status": "unhandled", "error": str(error)}
    
    def get_error_history(self) -> list:
        return self.error_log.copy()

_handler = None

def get_error_handler():
    global _handler
    if _handler is None:
        _handler = ErrorHandler()
    return _handler
