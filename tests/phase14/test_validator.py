import pytest
from jarvis.core.validation.validator import Validator

def test_add_rule():
    v = Validator()
    v.add_rule("name", "type", "str")
    assert "name" in v.rules

def test_validate():
    v = Validator()
    v.add_rule("email", "type", "str")
    valid, errors = v.validate({"email": "test@test.com"})
    assert valid

def test_validation_failure():
    v = Validator()
    v.add_rule("age", "min", 5)
    valid, errors = v.validate({"age": "ab"})
    assert not valid
