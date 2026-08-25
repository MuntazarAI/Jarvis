import pytest
from jarvis.core.distributed.node import Node, NodeManager

@pytest.fixture
def manager():
    return NodeManager()

def test_create_node():
    node = Node("n1", "worker")
    assert node.node_id == "n1"

def test_heartbeat():
    node = Node("n1")
    result = node.send_heartbeat()
    assert result["status"] == "alive"

def test_node_health():
    node = Node("n1")
    node.send_heartbeat()
    assert node.is_healthy()

def test_register_node(manager):
    node = Node("n1")
    manager.register_node(node)
    assert len(manager.nodes) == 1

def test_get_active_nodes(manager):
    node = Node("n1")
    manager.register_node(node)
    active = manager.get_active_nodes()
    assert len(active) == 1

def test_broadcast_state(manager):
    node = Node("n1")
    manager.register_node(node)
    manager.broadcast_state({"key": "value"})
    assert node.get_state()["key"] == "value"

def test_cluster_stats(manager):
    node = Node("n1")
    manager.register_node(node)
    stats = manager.get_cluster_stats()
    assert stats["total_nodes"] == 1
