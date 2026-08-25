import pytest
from jarvis.core.encryption.crypto import CryptoManager

def test_hash_password():
    crypto = CryptoManager()
    hashed = crypto.hash_password("password123")
    assert len(hashed) == 64

def test_verify_password():
    crypto = CryptoManager()
    hashed = crypto.hash_password("secret")
    assert crypto.verify_password("secret", hashed)

def test_encrypt():
    crypto = CryptoManager()
    encrypted = crypto.encrypt("data")
    assert len(encrypted) > 0
