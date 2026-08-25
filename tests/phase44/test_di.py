from jarvis.core.di.container import Container

def test_register():
    container = Container()
    container.register("service", lambda: {"name": "test"})
    assert container.has("service")

def test_get():
    container = Container()
    container.register("obj", lambda: {"value": 42})
    obj = container.get("obj")
    assert obj is not None
