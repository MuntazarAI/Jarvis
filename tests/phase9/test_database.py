import pytest
from jarvis.core.database.storage import get_database

@pytest.fixture
def db():
    return get_database()

def test_insert(db):
    db.insert("users", "u1", {"name": "Alice"})
    record = db.query("users", "u1")
    assert record["name"] == "Alice"

def test_update(db):
    db.insert("users", "u1", {"name": "Alice"})
    db.update("users", "u1", {"age": 30})
    record = db.query("users", "u1")
    assert record["age"] == 30

def test_delete(db):
    db.insert("users", "u1", {"name": "Alice"})
    db.delete("users", "u1")
    record = db.query("users", "u1")
    assert record == {}

def test_db_stats(db):
    db.insert("users", "u1", {"name": "Alice"})
    stats = db.get_stats()
    assert stats["tables"] > 0
