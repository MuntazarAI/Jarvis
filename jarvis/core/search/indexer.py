from typing import Dict, List

class SearchIndex:
    def __init__(self):
        self.index = {}
    
    def add(self, doc_id: str, content: str):
        words = content.lower().split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            if doc_id not in self.index[word]:
                self.index[word].append(doc_id)
    
    def search(self, query: str) -> List[str]:
        words = query.lower().split()
        if not words:
            return []
        
        results = set(self.index.get(words[0], []))
        for word in words[1:]:
            results &= set(self.index.get(word, []))
        return list(results)
    
    def remove(self, doc_id: str):
        for word in self.index:
            if doc_id in self.index[word]:
                self.index[word].remove(doc_id)

_index = None

def get_search_index():
    global _index
    if _index is None:
        _index = SearchIndex()
    return _index
