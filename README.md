# Extra Files

This repository is used for storing any files I create to solve any CTF challenges or online practice

Labeling convention: **Event Platform - Name of Event/Challenge**

| Platform               | Acronym |
|------------------------|---------|
| In Person Event        | ip      |
| TryHackMe              | thm     |
| CryptoHack             | ch      |
| OverTheWire            | otw     |
| PicoCTF                | pctf    |

<br>

## Related Challenges and Files
### Madness - TryHackMe
- **thm-Madness.py**: Python file used for finding the required secret number during the challenge
- Read more about the program and challenge on my blog, [Madness Writeup - TryHackMe](https://cdenton1.github.io/2024/12/26/Madness-Writeup-TryHackMe.html)
### Introduction to CryptoHack - CryptoHack
- **XORprop.py**: XOR Properties, computing the flag from 4 provided hex strings using XOR
- **faveByte.py**: Favourite Byte, decrypting provided hex-encoded string to find the flag
### That's The Ticket - TryHackMe
- **thm-That'sTheTicket.py**: Python file used for brute-forcing into an admin's email account
- Read more about the program and challenge on my blog, [That's The Ticket Writeup - TryHackMe](https://cdenton1.github.io/2025/01/01/That's-The-Ticket-Writeup-TryHackMe.html)
### MagpieCTF 2025 - In Person Event
- **All-Ends-Same.py**: All Ends Same, RSA crypto challenge to retrieve the flag using the provided private key
- **Grey-Area.py**: Grey Area, decrypt the ciphertext via the factoring n attack method
- **Imp3rf3ct.py**: Imp3rf3ct, decrypt the ciphertext via the cube root attack method
- **Inverse-Converse.py**: Inverse Converse, decrypt the ciphertext using the provided c and k values
- Read more about each challenge on my blog, [MagpieCTF 2025](https://cdenton1.github.io/2025/02/28/MagpieCTF-25.html)
### Bandit - OverTheWire
- **bandit24.sh**: Shell script used for completing level 23 -> 24
- **bandit25.sh**: Shell script used for completing level 24 -> 25
- **bandit25-a2.sh**: More complex shell script for completing level 24 -> 25
- Read about my experience and writeup for each level on my blog, [Bandit Writeup - OverTheWire](https://cdenton1.github.io/2025/05/19/Bandit-Writeup-OverTheWire.html)
### Vault Door Series - PicoCTF
- **vd1-solution.py**: Converted an array from Java into Python to reconstrust the scrambled password
- **vd3-solution.py**: Reversed engineered Java source code to reconstrust the password
- **vd4-asciiToText.py**: Convert ascii output from another command into human readable text
- **vd5-solution.py**: Take the encoded string, decode from base64 and then url decode it, and print the password 
