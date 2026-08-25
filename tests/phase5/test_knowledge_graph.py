import pytest
from jarvis.core.knowledge.knowledge_graph import get_knowledge_graph

@pytest.fixture
def graph():
    return get_knowledge_graph()

def test_add_entity(graph):
    graph.add_entity("e1", "person", {"name": "Alice"})
    entity = graph.entities["e1"]
    assert entity["type"] == "person"

def test_add_relationship(graph):
    graph.add_entity("e1", "person")
    graph.add_entity("e2", "skill")
    graph.add_relationship("e1", "e2", "has_skill")
    assert len(graph.relationships) > 0

def test_get_neighbors(graph):
    graph.add_entity("e1", "person")
    graph.add_entity("e2", "skill")
    graph.add_relationship("e1", "e2", "has_skill")
    neighbors = graph.get_entity_neighbors("e1")
    assert len(neighbors) > 0

def test_graph_stats(graph):
    graph.add_entity("e1", "person")
    stats = graph.get_graph_stats()
    assert stats["entities"] >= 1
