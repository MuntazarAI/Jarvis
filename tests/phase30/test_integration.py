import pytest
from jarvis.core.integration.integrator import IntegrationManager

def test_register_integration():
    manager = IntegrationManager()
    integration = manager.register_integration("slack", "messaging")
    assert manager.get_integration("slack") is not None

def test_connect_integration():
    manager = IntegrationManager()
    integration = manager.register_integration("github", "vcs")
    integration.connect({"token": "abc123"})
    assert integration.is_connected()

def test_list_integrations():
    manager = IntegrationManager()
    manager.register_integration("i1", "type1")
    manager.register_integration("i2", "type2")
    integrations = manager.list_integrations()
    assert len(integrations) >= 2
