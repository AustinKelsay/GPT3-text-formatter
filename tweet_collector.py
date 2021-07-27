import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

headers = {'Authorization': f"Bearer {TOKEN}"}
params = {"exclude": 'retweets',"exclude": "replies", "max_results": "100", "pagination_token": '7140dibdnow9c7btw3w4dhblnqvsmhd4ucvum49r9ge9d'}
r = requests.get('https://api.twitter.com/2/users/745273/tweets', headers=headers , params=params)

data = r.json()["data"]

with open('tweets.json', 'w') as f:
    for obj in data:
        json.dump(obj, f)
        f.write("\n")