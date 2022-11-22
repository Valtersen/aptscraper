import requests
import scrapy
import json

from .. import settings


class AptScraperSpider(scrapy.Spider):
    name = 'apt_scraper'
    allowed_domains = ['www.kijiji.ca']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(AptScraperSpider, self).__init__(*args, **kwargs)
        self.start_urls.append(kwargs.get('url'))

    def get_phone(self, token):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': settings.USER_AGENT
                   }
        response = requests.get('https://www.kijiji.ca/j-vac-phone-get.json?token=' + token, headers=headers)
        return response.json()['phone']

    def parse(self, response):

        apartment = {'url': response.url}
        script = response.xpath(
            '//div[@id="FesLoader"]/script[@type="text/javascript"]/text()').get().replace('window.__data=', '')
        script = script.replace(';', '')
        script_json = dict(json.loads(script))
        apartment['id'] = script_json['config']['VIP']['adId']
        apartment['city'] = script_json['config']['searchForm']['locationName']
        apartment['title'] = script_json['config']['adInfo']['title']
        apartment['description'] = script_json['config']['VIP']['description']
        apartment['posted'] = response.xpath('//div[starts-with(@class, "datePosted")]/time/@datetime').get()
        apartment['location'] = script_json['config']['VIP']['adLocation']['mapAddress']
        apartment['owner_id'] = script_json['config']['VIP']['posterId']
        name = script_json['config']['VIP']['sellerName']
        apartment['owner_name'] = name if name else script_json['config']['profile']["postersCompanyName"]
        if 'phoneToken' in script_json['config']['profile']:
            apartment['owner_phone'] = self.get_phone(script_json['config']['profile']['phoneToken'])
        else:
            apartment['owner_phone'] = None
        price = script_json['config']['VIP']['price']['amount'] / 100
        apartment['price'] = price
        ad_attributes = script_json['config']['VIP']['adAttributes']
        for atr in ad_attributes:
            key = atr['machineKey']
            val = atr['machineValue']
            if key == 'numberbathrooms':
                val = float(val)/10
            apartment[key] = val

        yield apartment

