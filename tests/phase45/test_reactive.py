from jarvis.core.reactive.observable import Observable

def test_subscribe():
    obs = Observable()
    received = []
    obs.subscribe(lambda x: received.append(x))
    obs.emit(1)
    assert len(received) > 0

def test_emit():
    obs = Observable()
    values = []
    obs.subscribe(lambda x: values.append(x))
    obs.emit("test")
    assert values[0] == "test"
