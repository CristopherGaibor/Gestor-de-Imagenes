import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


SECRET_KEY = os.getenv("AES_SECRET_KEY", "12345678901234567890123456789012").encode()
IV = os.getenv("AES_IV", "1234567890123456").encode()

def encrypt_password_aes(password: str) -> str:
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(password.encode()) + padder.finalize()
    
    
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    
    return base64.b64encode(ciphertext).decode()

def decrypt_password_aes(ciphertext_str: str) -> str:
    ciphertext = base64.b64decode(ciphertext_str.encode())
    
   
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
    
    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted.decode()