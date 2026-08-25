from jarvis.core.final.engine import JARVISEngine

def test_init():
    engine = JARVISEngine()
    engine.init()
    assert engine.initialized

def test_start():
    engine = JARVISEngine()
    engine.init()
    assert engine.start()

def test_status():
    engine = JARVISEngine()
    engine.init()
    status = engine.get_status()
    assert status["initialized"]
