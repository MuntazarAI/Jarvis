import pytest
from jarvis.core.distributed.node import Node, NodeManager
from jarvis.core.distributed.task_distribution import TaskDistributor

@pytest.fixture
def distributor():
    manager = NodeManager()
    node = Node("n1")
    manager.register_node(node)
    return TaskDistributor(manager)

def test_submit_task(distributor):
    task = distributor.submit_task("t1", "compute", {"data": "test"})
    assert task.task_id == "t1"

def test_distribute_task(distributor):
    distributor.submit_task("t1", "compute", {"data": "test"})
    result = distributor.distribute_task("t1")
    assert result == True

def test_task_status(distributor):
    distributor.submit_task("t1", "compute", {"data": "test"})
    distributor.distribute_task("t1")
    status = distributor.get_task_status("t1")
    assert status["status"] == "assigned"

def test_distribution_stats(distributor):
    distributor.submit_task("t1", "compute", {"data": "test"})
    distributor.distribute_task("t1")
    stats = distributor.get_distribution_stats()
    assert stats["total_tasks"] == 1
