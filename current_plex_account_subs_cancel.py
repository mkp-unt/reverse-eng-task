import requests
import os
import json


# User input
# password = "correct-password"
# token = "your-valid-x-plex-token"

password = ""
token = ""

url = "https://plex.tv/api/v2/billing/cancel/remotewatchpass"
params = {
    "password": password,
    "token": token
}

headers = {
    "X-Plex-Product": "Plex Mediaverse",
    "X-Plex-Client-Identifier": "",
    "X-Plex-Language": "en-GB",
    "X-Plex-Platform-Version": "136.0.0.0",
    "X-Plex-Token": token,
    "X-Plex-Platform": "Chrome",
    "X-Plex-Device": "Linux",
    "X-Plex-Provider-Version": "6.5.0",
    "Origin": "https://account.plex.tv",
    "Referer": "https://account.plex.tv/",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

response = requests.delete(url, headers=headers, params=params)

print("Status:", response.status_code)
print("Response:", response.text)

# with open(r"next_output.json", "w") as file:
#     json.dump(response.json(), file, indent=4)
