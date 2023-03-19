from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

message = input('Enter a message to encrypt: ')
nonce, ciphertext, tag = encrypt(message)
print(f'Nonce: {nonce.hex()}')
print(f'Ciphertext: {ciphertext.hex()}')
print(f'Tag: {tag.hex()}')
print(f'Key: {key.hex()}')

# Open the file in write mode
with open('input.txt', 'wb') as file:
    # Write the key, nonce, tag, and ciphertext to the file on separate lines
    file.write(key + b'\n')
    file.write(nonce + b'\n')
    file.write(tag + b'\n')
    file.write(ciphertext)

print('Values written to input.txt')
