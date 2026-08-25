import pytest
from jarvis.core.config.settings import get_config

def test_set_get():
    cfg = get_config()
    cfg.set("test_key", "test_value")
    assert cfg.get("test_key") == "test_value"

def test_get_all():
    cfg = get_config()
    all_cfg = cfg.get_all()
    assert "host" in all_cfg

def test_validate():
    cfg = get_config()
    assert cfg.validate() == True
