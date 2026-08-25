from typing import Dict, List

class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []
    
    def insert(self, table: str, record_id: str, data: Dict) -> bool:
        if table not in self.data:
            self.data[table] = {}
        self.data[table][record_id] = data
        self.transactions.append({"op": "insert", "table": table, "id": record_id})
        return True
    
    def query(self, table: str, record_id: str = None) -> Dict:
        if table not in self.data:
            return {}
        if record_id:
            return self.data[table].get(record_id, {})
        return self.data[table]
    
    def update(self, table: str, record_id: str, data: Dict) -> bool:
        if table in self.data and record_id in self.data[table]:
            self.data[table][record_id].update(data)
            self.transactions.append({"op": "update", "table": table, "id": record_id})
            return True
        return False
    
    def delete(self, table: str, record_id: str) -> bool:
        if table in self.data and record_id in self.data[table]:
            del self.data[table][record_id]
            self.transactions.append({"op": "delete", "table": table, "id": record_id})
            return True
        return False
    
    def get_stats(self) -> Dict:
        return {"tables": len(self.data), "transactions": len(self.transactions)}

_db = None

def get_database():
    global _db
    if _db is None:
        _db = Database()
    return _db
