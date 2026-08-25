import time
from typing import Dict

class Backup:
    def __init__(self, backup_id: str, data: Dict):
        self.backup_id = backup_id
        self.data = data
        self.timestamp = time.time()
    
    def get_size(self) -> int:
        return len(str(self.data))

class BackupManager:
    def __init__(self):
        self.backups = {}
    
    def create_backup(self, backup_id: str, data: Dict) -> bool:
        self.backups[backup_id] = Backup(backup_id, data)
        return True
    
    def restore_backup(self, backup_id: str) -> Dict:
        if backup_id in self.backups:
            return self.backups[backup_id].data
        return {}
    
    def delete_backup(self, backup_id: str) -> bool:
        if backup_id in self.backups:
            del self.backups[backup_id]
            return True
        return False
    
    def list_backups(self) -> list:
        return list(self.backups.keys())

_manager = None

def get_backup_manager():
    global _manager
    if _manager is None:
        _manager = BackupManager()
    return _manager
