from jarvis.core.registry.service_registry import ServiceRegistry

def test_register():
    registry = ServiceRegistry()
    registry.register("api", "1.0", "http://api:8000")
    assert registry.lookup("api") is not None

def test_list():
    registry = ServiceRegistry()
    registry.register("s1", "1.0", "url1")
    assert len(registry.list_services()) > 0
