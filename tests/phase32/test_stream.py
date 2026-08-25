import pytest
from jarvis.core.streaming.stream import StreamManager

def test_create_stream():
    manager = StreamManager()
    stream = manager.create_stream("events")
    assert manager.get_stream("events") is not None

def test_publish():
    manager = StreamManager()
    stream = manager.create_stream("s1")
    stream.publish({"data": "test"})
    items = stream.get_items()
    assert len(items) > 0

def test_subscribe():
    manager = StreamManager()
    stream = manager.create_stream("s2")
    received = []
    stream.subscribe(lambda item: received.append(item))
    stream.publish({"key": "value"})
    assert len(received) > 0
