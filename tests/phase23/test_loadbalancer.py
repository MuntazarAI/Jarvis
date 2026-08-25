import pytest
from jarvis.core.loadbalancing.balancer import LoadBalancer

def test_round_robin():
    lb = LoadBalancer(["s1", "s2", "s3"])
    assert lb.get_next() == "s1"
    assert lb.get_next() == "s2"
    assert lb.get_next() == "s3"

def test_add_server():
    lb = LoadBalancer(["s1"])
    lb.add_server("s2")
    servers = lb.get_servers()
    assert len(servers) == 2

def test_remove_server():
    lb = LoadBalancer(["s1", "s2"])
    lb.remove_server("s1")
    assert lb.get_next() == "s2"
