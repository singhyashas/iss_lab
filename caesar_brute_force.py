def caesar_brute_force(cipher_text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = cipher_text.upper()

    for key in range(1, 26):
        decrypted_text = ''
        for char in cipher_text:
            if char in alphabet:
                idx = (alphabet.index(char) - key) % 26
                decrypted_text += alphabet[idx]
            else:
                decrypted_text += char  # keep non-alphabet characters as they are
        print(f"Key {key}: {decrypted_text}")

# Example usage
cipher = "WKH HDJOH KDV ODQGHG"
caesar_brute_force(cipher)
