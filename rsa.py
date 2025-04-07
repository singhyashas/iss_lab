from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Generate RSA keys (private and public)
def generate_rsa_keys():
    key = RSA.generate(2048)  # 2048-bit RSA key
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA Encryption
def rsa_encrypt(public_key, plaintext):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode('utf-8')

# RSA Decryption
def rsa_decrypt(private_key, ciphertext):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    ciphertext = base64.b64decode(ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()

    plaintext = "This is a secret message"

    # Encrypt the message with the public key
    encrypted_message = rsa_encrypt(public_key, plaintext)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message with the private key
    decrypted_message = rsa_decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
