# Athena Steganography Tool

Athena is a powerful steganography tool that allows users to securely hide and extract encrypted messages within images using **AES encryption** and **LSB (Least Significant Bit) steganography**.

## Features
- 🔒 **AES-256 Encryption** for secure message encoding
- 🖼️ **LSB Steganography** for discreet message hiding
- 🛠️ **Command Line Interface (CLI)** for easy interaction
- 🚀 **Fast and efficient** message embedding and extraction

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/O12KA/Athena
   cd Athena
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the tool using the command line:
```bash
python cli.py
```
Then, select an option from the menu:
1) Generate AES Key
2) Hide a Message in an Image
3) Extract a Message from an Image
4) Exit

### Example Commands
#### 🔹 Generate a Key
```bash
python cli.py
# Select option 1
```
#### 🔹 Hide a Message in an Image
```bash
python cli.py
# Select option 2
# Enter image path, message, and key
```
#### 🔹 Extract a Message from an Image
```bash
python cli.py
# Select option 3
# Enter image path and key file
```

## Notes
- Ensure you use a **PNG** image to avoid data loss.
- The tool supports **AES-256** encryption for secure communication.

## Todo
- 📂 **File encryption and hiding**
- 🎨 **GUI version**
- 🔄 **Multi-format support**

Enjoy using Athena! 🚀

