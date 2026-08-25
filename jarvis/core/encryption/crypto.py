import hashlib

class CryptoManager:
    def __init__(self):
        self.key = "secret_key"
    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        return self.hash_password(password) == hashed
    
    def encrypt(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()[:32]
    
    def generate_token(self, data: str) -> str:
        return hashlib.sha256((data + self.key).encode()).hexdigest()

_crypto = None

def get_crypto_manager():
    global _crypto
    if _crypto is None:
        _crypto = CryptoManager()
    return _crypto
