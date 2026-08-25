from typing import List, Dict

class SemanticSearch:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.search_history = []
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Semantic search across documents"""
        results = self.vector_store.search(query, top_k)
        self.search_history.append({"query": query, "results_count": len(results)})
        return results
    
    def retrieve_context(self, query: str, context_size: int = 3) -> str:
        """Retrieve context for RAG"""
        results = self.search(query, context_size)
        context = ""
        for result in results:
            doc = self.vector_store.get_document(result["doc_id"])
            if doc:
                context += f"[{result['doc_id']}]: {doc.get('text', '')}\n"
        return context
    
    def get_search_stats(self) -> Dict:
        return {"total_searches": len(self.search_history)}

_semantic_search = None

def get_semantic_search(vector_store):
    global _semantic_search
    if _semantic_search is None:
        _semantic_search = SemanticSearch(vector_store)
    return _semantic_search
