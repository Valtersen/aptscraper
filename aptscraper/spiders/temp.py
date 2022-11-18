import requests
from parsel import Selector
import json
from pprint import pprint


url = 'https://www.kijiji.ca/v-apartments-condos/edmonton/warm-pet-friendly-double-master-townhome-with-fenced-yard-garden/1637210119'
#     #'https://www.kijiji.ca/v-apartments-condos/edmonton/townhomes-with-in-suite-laundry-south-ridge-townhomes-townho/1635549115?siteLocale=en_CA'
# # url = 'https://www.kijiji.ca/v-apartments-condos/edmonton/townhomes-with-in-suite-laundry-south-ridge-townhomes-townho/1635549115?siteLocale=en_CA'
# #url = 'https://www.kijiji.ca/b-apartments-condos/edmonton/c37l1700203'
resp = requests.get(url)
#
selector = Selector(resp.text)
# #
# # print('NEXT: ', selector.xpath('//div[@class="pagination"]/a[@title="Next"]/@href').extract_first())
# # print('EXTRACTED LINKS: ')
# # print(selector.xpath('//div[@class="container-results large-images"]/div[@data-listing-id]/@data-vip-url').extract()[:3])
#
# apartment = {'url': url}
script = selector.xpath('//div[@id="FesLoader"]/script[@type="text/javascript"]/text()').extract_first().replace('window.__data=', '')
script = script.replace(';', '')
# #
script_json = dict(json.loads(script))
#pprint(script_json, sort_dicts=False)

# # ID
# apartment['id'] = script_json['config']['VIP']['adId']
#
# # TO DO -> CITY
# apartment['city'] = script_json['config']['searchForm']['locationName']
#
# # TITLE
# apartment['title'] = script_json['config']['adInfo']['title']

# DESCRIPTION
# apartment['description'] = script_json['config']['VIP']['description']
#
# # TO DO -> POSTED
# apartment["posted"] = selector.xpath('//div[starts-with(@class, "datePosted")]/time/@datetime').extract_first()
#
# # LOCATION
# apartment['location'] = script_json['config']['VIP']['adLocation']['mapAddress']
#
# # OWNER ID
# apartment['owner_id'] = script_json['config']['VIP']['posterId']
#
# # PRICE
# price = script_json['config']['VIP']['price']['amount']/100
# apartment['price'] = price
#
# ATTRIBUTES
# apartment['attrs'] = dict()
ad_attributes = script_json['config']['VIP']['adAttributes']
keys = []
for atr in ad_attributes:
#     #val = atr['localeSpecificValues']['en']['value'] if atr['localeSpecificValues']['en']['value'] else atr['machineValue']
#     key = atr['localeSpecificValues']['en']['label']
     key = atr['machineKey']
     keys += [key]
print(keys)

    # #val = atr['machineValue']
    # key_verbose = atr['localeSpecificValues']['en']['label']
    # apartment['attrs'][key] = val


# pprint(apartment['attrs'], sort_dicts=False)
# print('-------------------------------------------------------------------')
# print(apartment)