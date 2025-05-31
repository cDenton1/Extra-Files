# This file was used in the PicoCTF Vault Door Series challenge, vault-door-3, https://play.picoctf.org/playlists/13?m=83, and was written by cDenton1 (me)
# Taken Java source code, converted it to Python to reverse engineer to reconstruct the password of the vault (the flag for the challenge) 

def checkPw(pw):
    
    if len(pw) != 32:              # checks the password length is 32
        return False               # returns false if not
    buffer = [""] * 32             # creates a buffer list with 32 empty strings
    
    for i in range(8):             # copies the first 8 characters of the input to the buffer
        buffer[i] = pw[i]
    
    for i in range(8, 16):         # buffer 8 to 16 is filled with the reverse of pw 8 to 16
        buffer[i] = pw[23 - i]
        
    for i in range(16, 32, 2):     # the even indices of buffer 16 to 32 is filled with the reverse of pw 16 to 32
        buffer[i] = pw[46 - i]
    
    for i in range(31, 16, -2):    # the odd indices of buffer 17 to 32 is filled with the corresponding pw i
        buffer[i] = pw[i]
        
    final_pw = ''.join(buffer)     # combined the characters in the buffer list
    print(final_pw)                # prints the final descrambled password
    
checkPw("jU5t_a_sna_3lpm18g947_u_4_m9r54f")
