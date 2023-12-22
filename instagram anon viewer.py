# instagram anon viewer 


import requests

ACCESS_TOKEN = input("Enter your Instagram API access code: ")
USER_ID = input("Enter your targets Instagram Username: ")

# Get user's media
url = f'https://graph.instagram.com/v13.0/{USER_ID}?fields=id,media&access_token={ACCESS_TOKEN}'

response = requests.get(url)
data = response.json()

# Process the data as needed
print(data)