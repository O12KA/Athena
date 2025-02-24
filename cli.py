import base64
import os
import sys
import time
from AES_encryption import encrypt_data, decrypt_data, generate_key
from LSB import encode_image, decode_image

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_aes_key():
    key = generate_key()
    with open("key.bin", "wb") as key_file:
        key_file.write(key)
    print("✅ AES Key generated and saved as 'key.bin'.")
    time.sleep(2)

def hide_message():
    input_image = input("Enter input image path: ")
    output_image = input("Enter output image path: ")
    message = input("Enter the secret message: ")
    key_path = input("Enter the key file path: ")
    
    if not os.path.exists(input_image):
        print("❌ Error: The image file was not found!")
        return
    if not os.path.exists(key_path):
        print("❌ Error: The key file was not found!")
        return
    
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    
    encrypted_data = encrypt_data(message, key)
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode()
    encode_image(input_image, encrypted_data_base64, output_image)
    print(f"✅ Secret message hidden in {output_image}")
    time.sleep(2)

def extract_message():
    image_path = input("Enter the image path: ")
    key_path = input("Enter the key file path: ")
    
    if not os.path.exists(image_path):
        print("❌ Error: The image file was not found!")
        return
    if not os.path.exists(key_path):
        print("❌ Error: The key file was not found!")
        return
    
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    
    extracted_data = decode_image(image_path)
    if not extracted_data:
        print("❌ No hidden data found!")
        return
    
    try:
        decrypted_data = decrypt_data(base64.b64decode(extracted_data), key)
        print(f"✅ Extracted message: {decrypted_data}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    time.sleep(2)

def main_menu():
    while True:
        clear_screen()
        print("Welcome to Athena Steganography Tool!")
        print("Please choose an option:")
        print("1) Generate AES Key")
        print("2) Hide a Message in an Image")
        print("3) Extract a Message from an Image")
        print("4) Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            generate_aes_key()
        elif choice == "2":
            hide_message()
        elif choice == "3":
            extract_message()
        elif choice == "4":
            print("Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice, please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()
