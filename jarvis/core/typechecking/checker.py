from typing import Dict, Any

class TypeValidator:
    def __init__(self):
        self.type_rules = {}
    
    def register_type(self, type_name: str, type_class: type):
        self.type_rules[type_name] = type_class
    
    def validate(self, value: Any, expected_type: str) -> bool:
        if expected_type not in self.type_rules:
            return False
        expected_class = self.type_rules[expected_type]
        return isinstance(value, expected_class)
    
    def validate_dict(self, data: Dict, schema: Dict) -> tuple:
        errors = []
        for key, expected_type in schema.items():
            if key not in data:
                errors.append(f"Missing key: {key}")
            elif not self.validate(data[key], expected_type):
                errors.append(f"Invalid type for {key}")
        return len(errors) == 0, errors

_validator = None

def get_type_validator():
    global _validator
    if _validator is None:
        _validator = TypeValidator()
    return _validator
