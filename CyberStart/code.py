# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

with open("words.txt") as wordfile:
  for line in wordfile:

    secret = line.strip()

    if secret[-1:] == "\n":
        print("Error, new line character at the end of the string. This will not match!")
    else:
        try:
          if len(secret.encode('latin-1')) >= 32:
            continue
          # create a cipher object using the secret
          cipher = AES.new(secret + (BLOCK_SIZE - len(secret.encode('latin-1')) % BLOCK_SIZE) * PADDING, AES.MODE_ECB)

          # decode the encoded string
          
          decoded = decode_aes(cipher, encrypted)

          if decoded != "":
              print('Decoded: '+decoded+"\n")
             
        except:
          continue