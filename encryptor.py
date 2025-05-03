# encryptor.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, path):
    with open(path, 'wb') as f:
        f.write(key)

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()
