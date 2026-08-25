import pytest
from jarvis.core.knowledge.embeddings import get_embedding_model
from jarvis.core.knowledge.vector_store import VectorStore

@pytest.fixture
def store():
    model = get_embedding_model()
    return VectorStore(model)

def test_add_document(store):
    store.add_document("doc1", "This is a test", {"source": "test"})
    doc = store.get_document("doc1")
    assert doc["source"] == "test"

def test_search(store):
    store.add_document("doc1", "machine learning")
    store.add_document("doc2", "deep learning")
    store.add_document("doc3", "pizza recipe")
    results = store.search("learning", top_k=2)
    assert len(results) <= 2

def test_search_results(store):
    store.add_document("doc1", "AI is great")
    results = store.search("artificial intelligence")
    assert len(results) > 0
