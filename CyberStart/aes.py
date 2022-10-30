# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "npv+MQVzd37JQYt+ITWpGCYVsJeYTnIZKxonEO0+aa+6lzd/MzPw5xdf/pIVwZ8D"

def decode_aes(c, e):
    return c.decrypt(e).decode('latin-1').rstrip(PADDING)
# base64.b64decode(

vector = "7862747A63616B69647A6E62627A6178".decode("hex")
secret = "66666F62766264687677776262696B7400000000000000000000000000000000".decode("hex")
# secret = "66666F62766264687677776262696B7400000000000000000000000000000000".decode("hex")
# key = 73737c6f256f71752526266f6f7678230d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d
# iv = 8716A72626E6A74696B61636A7472687
# 


# create a cipher object using the secret
cipher = AES.new(secret, AES.MODE_CBC, iv=vector)
# + (BLOCK_SIZE - len(secret.encode('latin-1')) % BLOCK_SIZE) * PADDING
# decode the encoded string

# decoded = decode_aes(cipher, encrypted)
decoded = cipher.decrypt(base64.b64decode(encrypted)).decode("latin-1")

print('Decoded: '+decoded)
    