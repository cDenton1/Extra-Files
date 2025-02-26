from Crypto.PublicKey import RSA        # handle RSA keys
from Crypto.Cipher import PKCS1_OAEP    # handle OAEP padding
from base64 import b64decode            # handle base64-decoding

with open("private_key.pem", "rb") as f:      # opens private key file in binary mode
    privkey = RSA.import_key(f.read())        # reads file, imports RSA key, and stores it

with open("ciphertext.txt", "rb") as f:       # opens cipertext file in binary mode
    ciphertext = b64decode(f.read())          # reads file, decodes the b64-encoded text, and stores it

cipher = PKCS1_OAEP.new(privkey)         # create RSA cipher object using OAEP padding and the private key
plaintext = cipher.decrypt(ciphertext)    # using the just made cipher, decrypt the ciphertext to obtain the plaintext

print(plaintext.decode())    # print out the plaintext (flag)
