# Introduction to CryptoHack - XOR Properties 
# hex strings provided
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_ALL_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# decode from hex to bytes
KEY1 = bytes.fromhex(KEY1_hex)
KEY2_XOR_KEY1 = bytes.fromhex(KEY2_XOR_KEY1_hex)
KEY2_XOR_KEY3 = bytes.fromhex(KEY2_XOR_KEY3_hex)
FLAG_XOR_ALL = bytes.fromhex(FLAG_XOR_ALL_hex)

# compute KEY2
KEY2 = bytes([b1 ^ b2 for b1, b2 in zip(KEY2_XOR_KEY1, KEY1)])

# compute KEY3
KEY3 = bytes([b1 ^ b2 for b1, b2 in zip(KEY2_XOR_KEY3, KEY2)])

# compute FLAG
FLAG = bytes([b1 ^ b2 ^ b3 ^ b4 for b1, b2, b3, b4 in zip(FLAG_XOR_ALL, KEY1, KEY2, KEY3)])

# print the FLAG
print("FLAG:", FLAG.decode())
