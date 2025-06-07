# This file was used in the PicoCTF Vault Door Series challenge, vault-door-7, https://play.picoctf.org/playlists/13?m=87, and was written by cDenton1 (me)
# Taken the given integers, reversed the encoding process by them converting to binary, splitting into 4 bytes, converting to hexadecimal, and then converting to characters
# Repeated that for each int given, eventually combining them all into one string and printing

ogPass = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304867, 942695730, 942748212]
thePass = [""] * 8

for i in range (8):
    binPass = bin(ogPass[i])
    
    binStr = binPass[2:].zfill(32)
    
    byte1 = binStr[0:8]
    byte2 = binStr[8:16]
    byte3 = binStr[16:24]
    byte4 = binStr[24:32]

    hex1 = hex(int(byte1, 2))
    hex2 = hex(int(byte2, 2))
    hex3 = hex(int(byte3, 2))
    hex4 = hex(int(byte4, 2))
    
    char1 = chr(int(hex1, 16))
    char2 = chr(int(hex2, 16))
    char3 = chr(int(hex3, 16))
    char4 = chr(int(hex4, 16))
    
    buffer = [char1, char2, char3, char4]
    thePass[i] = ''.join(buffer)

pw = ''.join(thePass)
print(pw)
