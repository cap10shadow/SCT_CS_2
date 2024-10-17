# SCT_CS_2
Develop a simple image encryption tool using pixel manipulation .support operations like swapping pixel values or applying a basic mathematical operation to each pixel

# Image Encryption Tool

## overview 

This project is a simple image encryption tool that allows users to download an image from a URL, encrypt it by manipulating pixel values, and then decrypt it back to its original form. The encryption process involves swapping pixel values and applying basic mathematical operations.

## Features
- Download images from a specified URL.
- Encrypt images by manipulating pixel values.
- Decrypt images back to their original form.
- Display the original, encrypted, and decrypted images.

## Usage
1. Run the Script: Execute the script in your Python environment. The script contains a hardcoded URL for an image, which will be downloaded automatically.
2. View the Images: After running the script, the following images will be saved in the same directory:
   encrypted_image.png: The encrypted version of the original image.
   decrypted_image.png: The decrypted version of the image, which should match the original.

## Code Explanation
### Key Functions
- download_image(url): Downloads an image from the specified URL and returns the image data.
- encrypt_image(image_data): Encrypts the image by swapping the red and blue pixel values and applying a simple mathematical operation.
- decrypt_image(encrypted_img): Decrypts the image by reversing the operations performed during encryption.
- main(): The main function that orchestrates the downloading, encrypting, and decrypting of the image. It uses a hardcoded URL for demonstration purposes.
