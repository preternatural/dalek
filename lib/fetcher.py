"""Fetch web pages using Diffbot to remove boilerplate.

   Diffbot endpoint: http://www.diffbot.com/api/article?token=...&url=...

   Jeff Reynar, 2013
"""
from urllib2 import urlopen

DIFFBOT_URL = "http://www.diffbot.com/api/article?token="
DIFFBOT_TOKEN = "1a1781471e3fbc194d64461eb17c8821"

class Fetcher(object):
    def __init__(self):
        self.diffbot_url = DIFFBOT_URL + DIFFBOT_TOKEN + '&url='

    def fetch_text_from_url(self, url):
        # Todo(jeff): escape url?
        response = urlopen(self.diffbot_url + url)
        return response.read()
