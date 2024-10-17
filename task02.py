import requests
from PIL import Image
import io

def download_image(url):
    """Download an image from a URL."""
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to download image. Status code: {}".format(response.status_code))

def encrypt_image(image_data):
    """Encrypt the image by swapping pixel values."""
    img = Image.open(io.BytesIO(image_data))
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Swap red and blue channels and apply a simple operation
            encrypted_pixel = ((b + 50) % 256, g, (r - 50) % 256)
            pixels[x, y] = encrypted_pixel

    return img

def decrypt_image(encrypted_img):
    """Decrypt the image by reversing the encryption process."""
    pixels = encrypted_img.load()
    width, height = encrypted_img.size

    for x in range(width):
        for y in range(height):
            b, g, r = pixels[x, y]
            # Reverse the swap and operations
            decrypted_pixel = ((r + 50) % 256, g, (b - 50) % 256)
            pixels[x, y] = decrypted_pixel

    return encrypted_img

def main():
    #  URL of the image
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/330px-Image_created_with_a_mobile_phone.png"

    # Download the image
    image_data = download_image(url)

    # Encrypt the image
    encrypted_image = encrypt_image(image_data)
    encrypted_image.save("encrypted_image.png")
    print("Encrypted image saved as 'encrypted_image.png'")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image)
    decrypted_image.save("decrypted_image.png")
    print("Decrypted image saved as 'decrypted_image.png'")

    # Show images
    encrypted_image.show(title="Encrypted Image")
    decrypted_image.show(title="Decrypted Image")

if __name__ == "__main__":
    main()
