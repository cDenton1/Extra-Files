# This file was used in the PicoCTF Vault Door Series challenge, vault-door-1, https://play.picoctf.org/playlists/13?m=82, and was written by cDenton1 (me)
# Taken an array from Java, converted it to Python to reconstruct the password of the vault (the flag for the challenge) 

password = [''] * 32    #create a list of 32 empty characters

# list of chracters in the password to their position, converted from Java
password[0]  = 'd'
password[29] = '9'
password[4]  = 'r'
password[2]  = '5'
password[23] = 'r'
password[3]  = 'c'
password[17] = '4'
password[1]  = '3'
password[7]  = 'b'
password[10] = '_'
password[5]  = '4'
password[9]  = '3'
password[11] = 't'
password[15] = 'c'
password[8]  = 'l'
password[12] = 'H'
password[20] = 'c'
password[14] = '_'
password[6]  = 'm'
password[24] = '5'
password[18] = 'r'
password[13] = '3'
password[19] = '4'
password[21] = 'T'
password[16] = 'H'
password[27] = '5'
password[30] = '2'
password[25] = '_'
password[22] = '3'
password[28] = '0'
password[26] = '7'
password[31] = 'e'

final_pass = ''.join(password)    # combined each character in the list
print(final_pass)                 # printed the descrambled password
