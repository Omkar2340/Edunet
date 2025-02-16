import cv2
import numpy as np
import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key_from_password(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_data(data, password):
    key = generate_key_from_password(password)
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, password):
    key = generate_key_from_password(password)
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def bytes_to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_bytes(binary_str):
    return bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))

def embed_file(image_path, file_path, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("[!] Error: Could not load image.")
        return
    with open(file_path, "rb") as f:
        file_data = f.read()
    encrypted_data = encrypt_data(file_data, password)
    binary_data = bytes_to_binary(encrypted_data)
    data_len = len(binary_data)
    height, width, _ = img.shape
    if data_len > height * width * 3:
        print("[!] Error: File too large to hide in this image.")
        return
    idx = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):
                if idx < data_len:
                    img[i, j, k] = (img[i, j, k] & 0b11111110) | int(binary_data[idx])
                    idx += 1
                else:
                    break
            if idx >= data_len:
                break
        if idx >= data_len:
            break
    cv2.imwrite(output_path, img)
    print(f"[+] File hidden successfully in {output_path}")

def extract_file(image_path, password, output_file):
    img = cv2.imread(image_path)
    if img is None:
        print("[!] Error: Could not load image.")
        return
    height, width, _ = img.shape
    extracted_bits = ""
    for i in range(height):
        for j in range(width):
            for k in range(3):
                extracted_bits += str(img[i, j, k] & 1)
    extracted_bytes = binary_to_bytes(extracted_bits)
    try:
        file_data = decrypt_data(extracted_bytes, password)
    except Exception:
        print("[!] Error: Incorrect password or corrupted data.")
        return
    with open(output_file, "wb") as f:
        f.write(file_data)

    print(f"[+] File extracted successfully to {output_file}")
def main():
    print("""
    #####################################
    #         StegoShadow Tool         #
    #   Hide and Retrieve Messages!    #
    #####################################
    """)

    while True:
        print("\nOptions:\n1. Hide a file in an image\n2. Extract a file from an image\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            img_path = input("Enter input image path: ")
            file_path = input("Enter the file to hide: ")
            password = input("Enter encryption password: ")
            output_path = input("Enter output image path: ")

            embed_file(img_path, file_path, password, output_path)

        elif choice == "2":
            img_path = input("Enter stego image path: ")
            password = input("Enter decryption password: ")
            output_file = input("Enter output file path: ")

            extract_file(img_path, password, output_file)

        elif choice == "3":
            print("[+] Exiting program.")
            break
        else:
            print("[!] Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
