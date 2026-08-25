import hashlib

class EmbeddingModel:
    def __init__(self, model_name: str = "simple"):
        self.model_name = model_name
        self.embeddings_cache = {}
    
    def embed_text(self, text: str):
        """Generate embedding for text (simplified)"""
        if text in self.embeddings_cache:
            return self.embeddings_cache[text]
        hash_obj = hashlib.sha256(text.encode())
        hash_hex = hash_obj.hexdigest()
        embedding = [float(int(hash_hex[i:i+2], 16)) / 256.0 for i in range(0, 32, 2)]
        self.embeddings_cache[text] = embedding
        return embedding
    
    def similarity(self, emb1, emb2):
        """Calculate cosine similarity"""
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = sum(a ** 2 for a in emb1) ** 0.5
        norm2 = sum(b ** 2 for b in emb2) ** 0.5
        return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0.0

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = EmbeddingModel()
    return _model
