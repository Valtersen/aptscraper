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

    def get_phone_number(self, adId, sellerId, vipUrl, sellerName, listingType='rent'):
        payload = [{
            "operationName": "GetDynamicPhoneNumber",
            "variables": {"adId": str(adId), "sellerId": str(sellerId), "vipUrl": vipUrl, "listingType": listingType,
                          "sellerName": sellerName},
            "query": "query GetDynamicPhoneNumber($sellerId: String!, $adId: String!, $userId: String, $vipUrl: String!, "
                     "$listingType: String!, $sellerName: String!) {getDynamicPhoneNumber(sellerId: $sellerId, adId: $adId, "
                     "userId: $userId, vipUrl: $vipUrl, listingType: $listingType, sellerName: $sellerName) {local e164 __typename}}"
        }]
        headers = {'Content-Type': 'application/json',
                   'User-Agent': settings.USER_AGENT
                   }
        resp = requests.post('https://www.kijiji.ca/anvil/api', json=payload, headers=headers)
        if 'errors' in resp.json()[0]:
            return
        resp = resp.json()[0]['data']['getDynamicPhoneNumber']['local']
        return resp

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
        apartment['owner_phone'] = self.get_phone_number(apartment['id'], apartment['owner_id'],
                                                         apartment['url'], apartment['owner_name'])
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

