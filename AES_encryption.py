from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64

def generate_key():
    """توليد مفتاح AES 256-bit"""
    return get_random_bytes(32)

def encrypt_data(data, key):
    """تشفير البيانات باستخدام AES-GCM"""
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return cipher.nonce + tag + ciphertext  # نجمع كل الأجزاء

def decrypt_data(encrypted_data, key):
    """فك التشفير باستخدام AES-GCM"""
    try:
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
    except Exception as e:
        print(f"❌ خطأ أثناء فك التشفير: {e}")
        return None
