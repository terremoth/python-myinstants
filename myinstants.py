#!/usr/bin/env python

import urllib.parse
from requests import get
from bs4 import BeautifulSoup
from sys import argv
from tempfile import gettempdir
from time import sleep
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

term_arg = ' '.join(argv[1:])
term_parsed = urllib.parse.quote_plus(term_arg)

try:
    page = get(f"https://www.myinstants.com/en/search/?name={term_parsed}")
    if page.status_code == 200:
        parser = BeautifulSoup(page.content, 'html.parser')
        button = parser.find("button", {'class': 'small-button'}).get('onclick')
        button_args = button.replace('play(', '').replace(')', '').replace("'", '')
        file = button_args.split(", ")[0]
        file_url = f"https://www.myinstants.com{file}"
        true_complete_filename = file.split('/')[-1]
        get_file = get(file_url, allow_redirects=True)

        tmp_dir = gettempdir()
        complete_file_with_path = os.path.join(tmp_dir, true_complete_filename)
        file_handler = open(complete_file_with_path, 'wb')
        file_handler.write(get_file.content)
        file_handler.close()

        mixer.init()
        mixer.music.load(complete_file_with_path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            sleep(1)

        mixer.music.unload()

        if os.path.exists(complete_file_with_path):
            os.remove(complete_file_with_path)

    else:
        print("Failed to load page, because HTTP status code is:", page.status_code)

except Exception as e:
    print(e)

