from analysis.dependency_graph import dependency_graph


def test_build_graph():

    graph = dependency_graph.build(".")

    assert isinstance(graph, dict)
    assert len(graph) > 0


def test_every_node_has_required_fields():

    graph = dependency_graph.build(".")

    for info in graph.values():

        assert "imports" in info
        assert "classes" in info
        assert "functions" in info
        assert "used_by" in info