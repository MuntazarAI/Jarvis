from jarvis.core.patterns.singleton import Singleton, Factory

def test_singleton():
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2

def test_factory():
    factory = Factory()
    factory.register("type1", lambda: {"type": "1"})
    obj = factory.create("type1")
    assert obj is not None
