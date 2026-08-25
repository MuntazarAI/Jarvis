import pytest
from jarvis.core.knowledge.embeddings import get_embedding_model
from jarvis.core.knowledge.vector_store import VectorStore
from jarvis.core.knowledge.semantic_search import SemanticSearch
from jarvis.core.knowledge.rag_engine import RAGEngine

@pytest.fixture
def rag():
    model = get_embedding_model()
    store = VectorStore(model)
    store.add_document("doc1", "AI enables automation")
    search = SemanticSearch(store)
    return RAGEngine(search)

@pytest.mark.asyncio
async def test_generate_answer(rag):
    result = await rag.generate_answer("What is AI?")
    assert "query" in result
    assert "answer" in result

@pytest.mark.asyncio
async def test_confidence(rag):
    result = await rag.generate_answer("test query")
    assert result["confidence"] > 0

def test_rag_stats(rag):
    import asyncio
    asyncio.run(rag.generate_answer("query"))
    stats = rag.get_stats()
    assert stats["total_queries"] >= 1
