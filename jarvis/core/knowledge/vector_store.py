from typing import List, Dict

class VectorStore:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.vectors = {}
        self.metadata = {}
    
    def add_document(self, doc_id: str, text: str, metadata: Dict = None):
        """Add document with embedding"""
        embedding = self.embedding_model.embed_text(text)
        self.vectors[doc_id] = embedding
        self.metadata[doc_id] = metadata or {"text": text}
    
    def search(self, query: str, top_k: int = 5):
        """Search for similar documents"""
        query_emb = self.embedding_model.embed_text(query)
        scores = []
        for doc_id, doc_emb in self.vectors.items():
            similarity = self.embedding_model.similarity(query_emb, doc_emb)
            scores.append({"doc_id": doc_id, "score": similarity})
        scores.sort(key=lambda x: x["score"], reverse=True)
        return scores[:top_k]
    
    def get_document(self, doc_id: str):
        return self.metadata.get(doc_id)

_store = None

def get_vector_store(embedding_model):
    global _store
    if _store is None:
        _store = VectorStore(embedding_model)
    return _store
