"""Fetch and print current Plex account details."""

import os
import json
import uuid
import requests

PLEX_TOKEN = "" 
CLIENT_ID   = "" # or str(uuid.uuid4())

BASE = "https://plex.tv"
URL  = f"{BASE}/api/v2/user/subscriptions"

HEADERS = {
    "Accept": "application/json",
    "X-Plex-Token": PLEX_TOKEN,
    "X-Plex-Client-Identifier": CLIENT_ID,
    "User-Agent": "PlexSubDemo/1.0",
}

resp = requests.get(URL, headers=HEADERS, timeout=10)
resp.raise_for_status()            # 4xx/5xx

subs = resp.json()
print(json.dumps(subs, indent=2))

with open(r"output3.json", "w") as file:
    json.dump(subs, file, indent=4)
