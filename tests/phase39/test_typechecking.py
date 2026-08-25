import pytest
from jarvis.core.typechecking.checker import TypeValidator

def test_register_type():
    validator = TypeValidator()
    validator.register_type("integer", int)
    assert validator.validate(42, "integer")

def test_validate():
    validator = TypeValidator()
    validator.register_type("string", str)
    assert validator.validate("hello", "string")

def test_validate_dict():
    validator = TypeValidator()
    validator.register_type("int", int)
    validator.register_type("str", str)
    schema = {"age": "int", "name": "str"}
    data = {"age": 25, "name": "Alice"}
    valid, errors = validator.validate_dict(data, schema)
    assert valid
