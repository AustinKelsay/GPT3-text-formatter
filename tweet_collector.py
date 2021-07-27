import requests
import os

TOKEN = os.getenv("TWITTER_TOKEN")

headers = {'Authorization': f"Bearer {TOKEN}"}
params = {"exclude": 'retweets'}
r = requests.get('https://api.twitter.com/2/users/745273/tweets', headers=headers , params=params)

print(r.json())