import requests
import scrapy
from requests.auth import HTTPBasicAuth

from .. import settings


def send_ad_link(link):
    payload = {
        "project": 'aptscraper',
        "spider": 'apt_scraper',
        "url": link
    }
    requests.post('http://'+settings.HOST+":6800/schedule.json", data=payload, auth=HTTPBasicAuth('debug', 'debug'))


class PageScraperSpider(scrapy.Spider):

    name = 'page_scraper'
    allowed_domains = ['www.kijiji.ca']
    start_urls = ['https://www.kijiji.ca/b-apartments-condos/charlottetown-pei/c37l1700119'
                  'https://www.kijiji.ca/b-apartments-condos/edmonton/c37l1700203',
                  'https://www.kijiji.ca/b-apartments-condos/winnipeg/c37l1700192',
                  'https://www.kijiji.ca/b-apartments-condos/victoria-bc/c37l1700173',
                  'https://www.kijiji.ca/b-apartments-condos/fredericton/c37l1700018',
                  'https://www.kijiji.ca/b-apartments-condos/st-johns/c37l1700113',
                  'https://www.kijiji.ca/b-apartments-condos/city-of-halifax/c37l1700321',
                  'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273',
                  'https://www.kijiji.ca/b-appartement-condo/ville-de-quebec/c37l1700124',
                  'https://www.kijiji.ca/b-apartments-condos/regina/c37l1700196', ]

    def parse(self, response):
        links = response.xpath(
            '//div[@class="container-results large-images"]/div[@data-listing-id]/@data-vip-url').getall()
        for link in links[:3]:
            full_link = 'https://www.kijiji.ca' + link
            send_ad_link(full_link)

        next_page = response.xpath('//div[@class="pagination"]/a[@title="Next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
