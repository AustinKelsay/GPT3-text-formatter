import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

headers = {'Authorization': f"Bearer {TOKEN}"}
params = {"exclude": 'replies', "max_results": "100"}
twitter_ids = [745273, 47966112, 221838349, 19721574, 375707743, 44196397, 83470331, 3289153303, 285636352, 16461706, 2853461537, 851773048973807617, 4885277053, 
824990584410476544, 1006521602769481728, 226428094, 998767132753125376, 23618940, 1003466586114494469, 14110443, 67109577, 2178012643, 95092020, 33152005, 358545917, 78683448, 
1010077800441765888, 447532101, 966562123, 2360241314, 1300971890, 846137120209190912, 55637356, 16906137, 23544268, 86993064, 14824849, 809760, 22461427, 4230121, 204832963, 1666038950]
tweets = []

for id in twitter_ids:
    r = requests.get(f"https://api.twitter.com/2/users/{id}/tweets", headers=headers , params=params)

    for obj in r.json()['data']:
        tweets.append(obj)


with open('tweets.json', 'w') as f:
        for obj in tweets:
            json.dump(obj, f)
            f.write("\n")