import numpy as np
import cv2

def encrypt_image(image_path, key):
    try:
        # Read the image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        if image is None:
            raise FileNotFoundError(f"Failed to read image '{image_path}'")

        # Convert image to numpy array of uint16 for safe manipulation
        image_array = np.array(image, dtype=np.uint16)

        # Encrypt each pixel value
        encrypted_array = (image_array + key) % 256

        # Convert back to uint8
        encrypted_image = encrypted_array.astype(np.uint8)

        return encrypted_image

    except Exception as e:
        print(f"Error occurred during encryption: {e}")
        return None

def decrypt_image(image_path, key):
    try:
        # Read the encrypted image
        encrypted_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        if encrypted_image is None:
            raise FileNotFoundError(f"Failed to read encrypted image '{image_path}'")

        # Convert image to numpy array of uint16 for safe manipulation
        encrypted_array = np.array(encrypted_image, dtype=np.uint16)

        # Decrypt each pixel value
        decrypted_array = (encrypted_array - key) % 256

        # Convert back to uint8
        decrypted_image = decrypted_array.astype(np.uint8)

        return decrypted_image

    except Exception as e:
        print(f"Error occurred during decryption: {e}")
        return None

def main():
    try:
        choice = int(input("Enter your choice (1 for encryption, 2 for decryption): "))
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Enter 1 for encryption or 2 for decryption.")

        image_path = input("Enter the path to the image file: ").strip('"')  # Remove extra quotes if present
        key = int(input("Enter the encryption/decryption key (an integer): "))

        if choice == 1:
            encrypted_image = encrypt_image(image_path, key)
            if encrypted_image is not None:
                cv2.imshow("Encrypted Image", encrypted_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Encryption failed.")

        elif choice == 2:
            decrypted_image = decrypt_image(image_path, key)
            if decrypted_image is not None:
                cv2.imshow("Decrypted Image", decrypted_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Decryption failed.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
