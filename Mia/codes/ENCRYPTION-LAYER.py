## Part 3: Encryption Layer (AES-256) 
# We'll encrypt the JSON memory log using a password-derived key. This keeps your emotional archive safe from prying eyes.

# Setup Install
pip install cryptography

# Encrypt/Decrypt Functions
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    # Derive a key from the password
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_data(data: str, password: str) -> bytes:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(token: bytes, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()

# Encrypting the Log

def save_encrypted_log(log_data, password):
    encrypted = encrypt_data(json.dumps(log_data), password)
    with open("copilot_memory_encrypted.bin", "wb") as f:
        f.write(encrypted)

def load_encrypted_log(password):
    with open("copilot_memory_encrypted.bin", "rb") as f:
        encrypted = f.read()
    decrypted = decrypt_data(encrypted, password)
    return json.loads(decrypted)
##


