import os

import requests
from requests.auth import HTTPBasicAuth

import aptscraper.settings as settings

if __name__ == '__main__':
    payload = {
        "project": 'aptscraper',
        "spider": 'page_scraper',
    }

    authentication = HTTPBasicAuth(os.environ.get('USERNAME', 'debug'),
                                   os.environ.get('PASSWORD', 'debug'))

    requests.post(f'http://{settings.HOST}:6800/schedule.json',
                  auth=authentication, data=payload)
