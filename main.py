import json
import config
from requests_oauthlib import OAuth1Session

CK = config.consumer_key
CS = config.consumer_secret
AT = config.access_token
AS = config.access_token_secret
twitter = OAuth1Session(CK, CS, AT, AS)

url = "https://api.twitter.com/1.1/blocks/ids.json"
res = twitter.get(url)

if res.status_code == 200:
    blocks = json.loads(res.text)
    ids = blocks["ids"]
    for id in ids:
        print("Unblock: %d" % id)
        url = "https://api.twitter.com/1.1/blocks/destroy.json"
        res = twitter.post(url, params = {"user_id" : id})
        if res.status_code == 200:
            print("Success.")
        else:
            print("Failed: %d %s" % (res.status_code, res.text))
else:
    print("Failed: %d %s" % (res.status_code, res.text))
