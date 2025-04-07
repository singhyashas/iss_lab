from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Generate a random 8-byte key (64-bit DES)
def generate_key():
    return get_random_bytes(8)

# DES Encryption
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ciphertext

# DES Decryption
def des_decrypt(key, iv, ciphertext):
    iv = base64.b64decode(iv)
    ciphertext = base64.b64decode(ciphertext)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    pt_bytes = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return pt_bytes.decode('utf-8')

# Example usage
if __name__ == "__main__":
    key = generate_key()
    plaintext = "This is a secret message"

    # Encrypt the message
    iv, encrypted_message = des_encrypt(key, plaintext)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = des_decrypt(key, iv, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
