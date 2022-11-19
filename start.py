import requests
from requests.auth import HTTPBasicAuth

import aptscraper.settings as settings

if __name__ == '__main__':

    payload = {
        "project": 'aptscraper',
        "spider": 'page_scraper',
    }
    requests.post(settings.HOST + ":6800/schedule.json", auth=HTTPBasicAuth('debug', 'debug'), data=payload)
