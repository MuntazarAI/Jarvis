from typing import Dict, Any

class Validator:
    def __init__(self):
        self.rules = {}
    
    def add_rule(self, field: str, rule_type: str, rule_value: Any = None):
        if field not in self.rules:
            self.rules[field] = []
        self.rules[field].append({"type": rule_type, "value": rule_value})
    
    def validate(self, data: Dict) -> tuple:
        errors = []
        for field, rules in self.rules.items():
            if field not in data:
                errors.append(f"{field} is required")
                continue
            
            value = data[field]
            for rule in rules:
                if rule["type"] == "type":
                    expected = rule["value"]
                    actual = type(value).__name__
                    if actual != expected:
                        errors.append(f"{field} must be {expected}, got {actual}")
                elif rule["type"] == "min":
                    if isinstance(value, str) and len(value) < rule["value"]:
                        errors.append(f"{field} must have min length {rule['value']}")
                    elif isinstance(value, (int, float)) and value < rule["value"]:
                        errors.append(f"{field} must be at least {rule['value']}")
        
        return len(errors) == 0, errors

_validator = None

def get_validator():
    global _validator
    if _validator is None:
        _validator = Validator()
    return _validator
