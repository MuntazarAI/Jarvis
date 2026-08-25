import pytest
from jarvis.core.backup.backup import BackupManager

def test_create_backup():
    bm = BackupManager()
    bm.create_backup("b1", {"key": "value"})
    assert "b1" in bm.list_backups()

def test_restore_backup():
    bm = BackupManager()
    bm.create_backup("b2", {"data": "test"})
    restored = bm.restore_backup("b2")
    assert restored["data"] == "test"

def test_delete_backup():
    bm = BackupManager()
    bm.create_backup("b3", {})
    assert bm.delete_backup("b3")
    assert "b3" not in bm.list_backups()
