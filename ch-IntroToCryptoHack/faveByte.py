# Introduction to CryptoHack - Favourite Byte

# given hex-encoded encrypted data
encrypted_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

encrypted_bytes = bytes.fromhex(encrypted_hex)                 # decode the hex string to bytes

for key in range(256):  # keys from 0x00 to 0xFF               # brute-force all possible single-byte keys
    decrypted = bytes([b ^ key for b in encrypted_bytes])      # XOR each byte in the encrypted data with the current key
    
    try:
        message = decrypted.decode('ascii')                    # try to decode as ASCII
        if "crypto" in message:                                # print readable outputs if they include crypto
            print(f"Key: {key} -> Message: {message}")
    except UnicodeDecodeError:
        pass                                                   # ignore non-readable outputs
