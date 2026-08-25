import pytest
from jarvis.core.knowledge.embeddings import get_embedding_model
from jarvis.core.knowledge.vector_store import VectorStore
from jarvis.core.knowledge.semantic_search import SemanticSearch

@pytest.fixture
def search():
    model = get_embedding_model()
    store = VectorStore(model)
    store.add_document("doc1", "Python programming")
    store.add_document("doc2", "JavaScript tutorial")
    return SemanticSearch(store)

def test_search_query(search):
    results = search.search("python")
    assert len(results) > 0

def test_retrieve_context(search):
    context = search.retrieve_context("programming")
    assert isinstance(context, str)

def test_search_stats(search):
    search.search("test")
    stats = search.get_search_stats()
    assert stats["total_searches"] >= 1
