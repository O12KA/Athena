from PIL import Image

def encode_image(image_path, secret_data, output_path):
    """إخفاء البيانات داخل الصورة باستخدام LSB"""
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    data_index = 0
    secret_data += "EOF"  # علامة نهاية البيانات
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_data)

    for y in range(height):
        for x in range(width):
            if data_index < len(binary_secret):
                pixel = list(img.getpixel((x, y)))
                for i in range(3):  # تعديل الـ RGB
                    if data_index < len(binary_secret):
                        pixel[i] = pixel[i] & ~1 | int(binary_secret[data_index])
                        data_index += 1
                encoded.putpixel((x, y), tuple(pixel))

    encoded.save(output_path)
    print(f"✅ تم إخفاء البيانات في الصورة: {output_path}")

def decode_image(image_path):
    """استخراج البيانات المخفية من الصورة"""
    img = Image.open(image_path)
    binary_data = ""
    
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            for i in range(3):
                binary_data += str(pixel[i] & 1)

    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    extracted_data = "".join(chr(int(char, 2)) for char in chars)
    
    if "EOF" in extracted_data:
        return extracted_data[:extracted_data.index("EOF")]
    else:
        print("❌ لم يتم العثور على بيانات صالحة!")
        return None
