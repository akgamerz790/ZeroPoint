#!/usr/bin/env python3
"""ZeroPoint Crypto Module - Educational Demo"""

import base64
from cryptography.fernet import Fernet

# Generate a key for demo purposes
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_data(data):
    """Encrypt string data"""
    if isinstance(data, str):
        data = data.encode()
    return cipher.encrypt(data)

def decrypt_data(encrypted_data):
    """Decrypt data back to string"""
    decrypted = cipher.decrypt(encrypted_data)
    return decrypted.decode()

def generate_key():
    """Generate new encryption key"""
    return Fernet.generate_key()