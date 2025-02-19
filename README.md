# StegoShadow - Hide and Retrieve Files in Images

StegoShadow is a Python-based steganography tool that allows you to hide files within images and extract them later. It uses encryption to secure the hidden data and embeds it in the least significant bits (LSBs) of the image pixels. This tool is perfect for securely sharing hidden messages or files without drawing attention.

## Features
- **Hide Files**: Embed any file (text, image, etc.) into an image.
- **Extract Files**: Retrieve hidden files from stego images.
- **Encryption**: Securely encrypt hidden data using a password.
- **User-Friendly**: Simple command-line interface for easy use.

## Requirements
- Python 3.x
- Libraries: opencv-python-headless, numpy, cryptography

## Installation
### Linux
```bash
sudo apt update
sudo apt install python3 python3-pip
git clone https://github.com/yourusername/StegoShadow.git
cd StegoShadow
pip install -r requirements.txt
sed -i 's/\r$//' main.py  # Ensure Unix-style line endings
chmod +x main.py
./main.py
```

### Windows
```bash
git clone https://github.com/yourusername/StegoShadow.git
cd StegoShadow
pip install -r requirements.txt
python main.py
```
## Usage

### Hide a File in an Image
1. Run the script:
```bash
./main.py
```
2. Choose option 1 to hide a file.

3. Provide the following inputs:
Input Image Path: The image in which the file will be hidden.
File to Hide: The file you want to hide (e.g., secret.txt).
Encryption Password: A password to encrypt the file.
Output Image Path: The path to save the stego image (e.g., output_image.png).

```Example
Enter input image path: input_image.png
Enter the file to hide: secret.txt
Enter encryption password: mypassword
Enter output image path: output_image.png
[+] File hidden successfully in output_image.png
```
### Extract a File from an Image
1. Run the script:
```bash
./main.py
```
2. Choose option 2 to extract a file.

3. Provide the following inputs:
Stego Image Path: The image containing the hidden file.
Decryption Password: The password used during encryption.
Output File Path: The path to save the extracted file (e.g., extracted_secret.txt).

```Example
Enter stego image path: output_image.png
Enter decryption password: mypassword
Enter output file path: extracted_secret.txt
[+] File extracted successfully to extracted_secret.txt
```

## How It Works
### Encryption
The file to be hidden is encrypted using the cryptography library's Fernet symmetric encryption. A password is used to generate a key, ensuring only authorized users can decrypt the data.

### Steganography
The encrypted file is converted into binary and embedded into the least significant bits (LSBs) of the image pixels. The extraction process reads the LSBs from the image, reconstructs the binary data, and decrypts it.

## Limitations
1. File Size: The file to be hidden must be small enough to fit in the image. The maximum size is approximately height * width * 3 / 8 bytes.
2. Password Security: The security of the hidden data relies on the strength of the password. Use strong passwords to prevent brute-force attacks.
3. Image Quality: Embedding data in the LSBs may slightly alter the image, but the changes are usually imperceptible.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Your Name: Omkar Khanolkar
GitHub: Omkar2340
