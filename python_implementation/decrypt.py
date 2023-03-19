from Crypto.Cipher import AES

# Read the input file
with open('input.txt', 'rb') as f:
    key = f.readline().strip()
    nonce = f.readline().strip()
    tag = f.readline().strip()
    ciphertext = f.read()

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print(f'Plaintext: {plaintext.decode("utf-8")}')
except ValueError:
    print('Message is corrupted')
