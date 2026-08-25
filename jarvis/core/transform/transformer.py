from typing import Callable, Dict

class Transformer:
    def __init__(self, name: str):
        self.name = name
        self.steps = []
    
    def add_step(self, func: Callable):
        self.steps.append(func)
    
    def transform(self, data):
        result = data
        for step in self.steps:
            result = step(result)
        return result

class TransformPipeline:
    def __init__(self):
        self.transformers = {}
    
    def create_transformer(self, name: str) -> Transformer:
        transformer = Transformer(name)
        self.transformers[name] = transformer
        return transformer
    
    def get_transformer(self, name: str) -> Transformer:
        return self.transformers.get(name)
    
    def apply(self, name: str, data):
        if name in self.transformers:
            return self.transformers[name].transform(data)
        return data
