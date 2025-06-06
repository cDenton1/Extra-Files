# This file was used in the PicoCTF Vault Door Series challenge, vault-door-5, https://play.picoctf.org/playlists/13?m=85, and was written by cDenton1 (me)
# Taken the given encoded string from the Java source code, decoded from base64 and url decoded it, and then printed the flag

import urllib.parse
import base64
    
encoded_string = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
print(encoded_string)

s1Decode_string = base64.b64decode(encoded_string)
s2Decode_string = urllib.parse.unquote(s1Decode_string)

print(s2Decode_string)
