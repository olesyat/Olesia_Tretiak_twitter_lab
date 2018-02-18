import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

acct = input('Enter Twitter Account:')
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '5'})
# print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)
# print(json.dumps(js, indent=2))

headers = dict(connection.getheaders())
# print('Remaining', headers['x-rate-limit-remaining'])
keys = [key for u in js['users'] for key in u]
print("Please choose one or more(seperetad) keywords from the following: ")
print(" ".join(keys))
kkeys = input(": ").split()
print(kkeys, kkeys[0])
for u in js['users']:
    print('screen_name: ', u['screen_name'])
    for k in kkeys:
        try:
            print(k+':', u[k])
        except KeyError:
            print(k, "sorry, no such keyword")
            continue
    print('\n')
