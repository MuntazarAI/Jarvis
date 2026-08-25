import pytest
from jarvis.core.knowledge.embeddings import get_embedding_model

def test_embed_text():
    model = get_embedding_model()
    emb1 = model.embed_text("hello world")
    assert len(emb1) == 16

def test_embed_consistency():
    model = get_embedding_model()
    emb1 = model.embed_text("test")
    emb2 = model.embed_text("test")
    assert emb1 == emb2

def test_similarity():
    model = get_embedding_model()
    emb1 = model.embed_text("hello")
    emb2 = model.embed_text("hello")
    sim = model.similarity(emb1, emb2)
    assert sim > 0.99
