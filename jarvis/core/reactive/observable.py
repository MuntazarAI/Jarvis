from typing import Callable, List

class Observer:
    def __init__(self, on_next: Callable):
        self.on_next = on_next
    
    def notify(self, value):
        self.on_next(value)

class Observable:
    def __init__(self):
        self.observers = []
    
    def subscribe(self, on_next: Callable) -> Observer:
        observer = Observer(on_next)
        self.observers.append(observer)
        return observer
    
    def emit(self, value):
        for observer in self.observers:
            observer.notify(value)
    
    def unsubscribe(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
