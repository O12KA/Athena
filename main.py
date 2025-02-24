import base64
from AES_encryption import encrypt_data, generate_key
from LSB import encode_image

# توليد مفتاح التشفير
key = generate_key()
with open("key.bin", "wb") as key_file:
    key_file.write(key)

print(f"🔑 تم حفظ المفتاح في 'key.bin'.")

# الرسالة اللي هنخفيها
message = "Hello Athena! This is a secret message."

# تشفير الرسالة
encrypted_data = encrypt_data(message, key)

# تحويل البيانات لـ Base64 قبل الإخفاء
encrypted_data_base64 = base64.b64encode(encrypted_data).decode()

# إخفاء البيانات في الصورة
input_image = "input.jpg"
output_image = "output.png"
encode_image(input_image, encrypted_data_base64, output_image)
