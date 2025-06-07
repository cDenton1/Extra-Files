# This file was used in the PicoCTF Vault Door Series challenge, vault-door-6, https://play.picoctf.org/playlists/13?m=86, and was written by cDenton1 (me)
# Taken the given bytes, taken the line, ((passBytes[i] ^ 0x55) - myBytes[i]) from the Java source code, converted the number to a character and stored it into a buffer list before printing 

myBytes = [0x3b, 0x65, 0x21, 0xa, 0x38, 0x0, 0x36, 0x1d, 0xa, 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa, 0x21, 0x1d, 0x61, 0x3b, 0xa, 0x2d, 0x65, 0x27, 0xa, 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c]
buffer = [""] * 32

for i in range (32):
    buffer[i] = chr(myBytes[i] ^ 0x55)
    
pw = ''.join(buffer)

if len(pw) != 32:
    print("ERROR:" + pw)
else:
    print(pw)
