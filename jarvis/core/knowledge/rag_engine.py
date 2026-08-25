from typing import Dict

class RAGEngine:
    def __init__(self, semantic_search, llm_model=None):
        self.semantic_search = semantic_search
        self.llm_model = llm_model
        self.queries = []
    
    async def generate_answer(self, query: str) -> Dict:
        """Generate answer using RAG"""
        context = self.semantic_search.retrieve_context(query)
        
        answer = {
            "query": query,
            "context": context,
            "answer": f"Based on context: {context[:100]}...",
            "confidence": 0.85
        }
        self.queries.append(answer)
        return answer
    
    def get_stats(self) -> Dict:
        return {"total_queries": len(self.queries)}

_rag_engine = None

def get_rag_engine(semantic_search, llm_model=None):
    global _rag_engine
    if _rag_engine is None:
        _rag_engine = RAGEngine(semantic_search, llm_model)
    return _rag_engine
