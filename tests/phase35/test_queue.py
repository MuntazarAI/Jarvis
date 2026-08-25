import pytest
from jarvis.core.messagequeue.queue import QueueManager

def test_create_queue():
    manager = QueueManager()
    queue = manager.create_queue("q1")
    assert manager.get_queue("q1") is not None

def test_enqueue_dequeue():
    manager = QueueManager()
    queue = manager.create_queue("q2")
    queue.enqueue("m1", {"data": "test"})
    msg = queue.dequeue()
    assert msg is not None

def test_queue_size():
    manager = QueueManager()
    queue = manager.create_queue("q3")
    queue.enqueue("m1", {})
    queue.enqueue("m2", {})
    assert queue.size() == 2
