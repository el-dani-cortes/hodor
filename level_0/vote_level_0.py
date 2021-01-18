#!/usr/bin/python3
"""Program to upload 1024 votes to level_0
of hodor project"""
import requests


# Request web page by get method
url = 'http://158.69.76.135/level0.php'
my_id = '2304'
params = {'id': my_id, 'holdthedoor': 'Submit'}
vote_success = 'Hold the Door challenge - Level 0'
r = requests.get(url)

# Loop to make the votes by post method
print("Uploading votes...")
vote = 1
while vote <= 1024:
    try:
        r = requests.post(url, data=params)
        if r.status_code is 200 and vote_success in r.text:
            print("Upload vote #{}".format(vote), end='\r', flush=True)
            vote += 1
    except Exception as error:
        print(error)
print("cheat online voting process ends :)")
