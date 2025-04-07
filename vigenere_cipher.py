def generate_key(text, keyword):
   key = list(keyword)
   if len(text) == len(keyword):
      return key
   else:
      for i in range(len(text) - len(keyword)):
         key.append(key[i % len(keyword)])
   return "".join(key)

def encrypt_text(text, key):
   cipher_text = []
   for i in range(len(text)):
      x = (ord(text[i]) + ord(key[i])) % 26
      x += ord('A')
      cipher_text.append(chr(x))
   return "".join(cipher_text)

def decrypt_text(cipher_text, key):
   original_text = []
   for i in range(len(cipher_text)):
      x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
      x += ord('A')
      original_text.append(chr(x))
   return "".join(original_text)

# Driver code
text = "TUTORIALSPOINT"
keyword = "KEY"
key = generate_key(text, keyword)
cipher_text = encrypt_text(text, key)
print("The Encrypted text:", cipher_text)
print("The Original/Decrypted Text:", decrypt_text(cipher_text, key))