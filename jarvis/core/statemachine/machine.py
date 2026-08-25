from typing import Dict, Callable

class State:
    def __init__(self, name: str):
        self.name = name

class StateMachine:
    def __init__(self, initial_state: str):
        self.current_state = initial_state
        self.states = {initial_state: State(initial_state)}
        self.transitions = {}
    
    def add_state(self, name: str):
        self.states[name] = State(name)
    
    def add_transition(self, from_state: str, to_state: str, event: str):
        key = f"{from_state}:{event}"
        self.transitions[key] = to_state
    
    def trigger(self, event: str) -> bool:
        key = f"{self.current_state}:{event}"
        if key in self.transitions:
            self.current_state = self.transitions[key]
            return True
        return False
    
    def get_current_state(self) -> str:
        return self.current_state
