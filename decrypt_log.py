def decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

with open("encrypted_keylog.txt", "r", encoding="utf-8") as f:
    encrypted = f.read()
    decrypted = decrypt(encrypted, 123)  # Use the same XOR key as in your logger
    print(decrypted)