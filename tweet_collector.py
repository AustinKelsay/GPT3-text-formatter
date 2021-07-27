import requests
import os

TOKEN = os.getenv("TWITTER_TOKEN")

headers = {'Authorization': f"Bearer {TOKEN}"}
r = requests.get('https://api.twitter.com/2/users/by/username/naval', headers=headers)

print(r.json())