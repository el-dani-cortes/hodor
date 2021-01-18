#!/usr/bin/python3
"""Program to upload 1024 votes to level_2
of hodor project"""
import requests

# Requests url and all its headers info by get method
url = 'http://158.69.76.135/level2.php'
my_id = '2304'
r = requests.get(url)
key = r.cookies['HoldTheDoor']
params = {'id': my_id, 'holdthedoor': 'Submit', 'key': key}
vote_success = 'Hold the Door challenge - Level 2'
cookie = {"HoldTheDoor": key}
# Assign header user-agent to only windows users
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": windows_user, "Referer": url}

# Loop to make 1024 votes by post method
print("Uploading votes...")
vote = 1
while vote <= 1024:
    response = requests.post(url, data=params, cookies=cookie, headers=header)
    if response.status_code is 200 and vote_success in r.text:
        vote += 1
        print("Upload vote #{}".format(vote), end='\r', flush=True)
    else:
        print("Fail vote #{}".format(vote), end='\r', flush=True)
print("cheat online voting process ends :)")
