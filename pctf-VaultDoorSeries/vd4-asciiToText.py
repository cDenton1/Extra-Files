# This file was used in the PicoCTF Vault Door Series challenge, vault-door-4, https://play.picoctf.org/playlists/13?m=84, and was written by cDenton1 (me)

# usage: convert ascii output from another command to readable text
# example: cat vd4Text.txt | python3 asciiText.py

import sys

def parse_token(token):
    token = token.strip()
    
    if token.startswith("0x"):
        return chr(int(token, 16))
    elif token.startswith("0"):
        return chr(int(token, 8))
    elif token.startswith("'") and token.endswith("'"):
        return token[1]
    else: 
        return chr(int(token))

def ascii_to_text(data):
    tokens = data.split()
    chars = [parse_token(token) for token in tokens]
    return ''.join(chars)
    
if __name__ == "__main__":
    input_data = sys.stdin.read()
    results = ascii_to_text(input_data)
    print(results)
