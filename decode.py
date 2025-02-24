import base64
from AES_encryption import decrypt_data
from LSB import decode_image

# تحميل المفتاح من الملف
with open("key.bin", "rb") as key_file:
    key = key_file.read()

# استخراج البيانات من الصورة
image_with_data = "output.png"
extracted_data = decode_image(image_with_data)

if extracted_data:
    print(f"🔍 البيانات المستخرجة (Base64): {extracted_data[:50]}...")

    # فك التشفير
    decrypted_data = decrypt_data(base64.b64decode(extracted_data), key)
    if decrypted_data:
        print(f"✅ الرسالة الأصلية: {decrypted_data}")
