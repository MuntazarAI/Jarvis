import pytest
from jarvis.core.search.indexer import get_search_index

def test_add_and_search():
    index = get_search_index()
    index.add("doc1", "hello world")
    results = index.search("hello")
    assert "doc1" in results

def test_multi_word_search():
    index = get_search_index()
    index.add("doc1", "hello world")
    index.add("doc2", "hello there")
    results = index.search("hello world")
    assert "doc1" in results

def test_remove():
    index = get_search_index()
    index.add("doc1", "test content")
    index.remove("doc1")
    results = index.search("test")
    assert len(results) == 0
