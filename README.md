# Apartment scraper

Parse rent long term rent ads from  https://www.kijiji.ca/ for all Canadian provinces and their capitals.

Using Scrapy and Scrapyd for parsing, Postgres database and FastAPI.

scrapyd-authenticated from :
https://github.com/namiwa/scrapyd-authenticated


```git clone https://github.com/Valtersen/aptscraper```


```docker-compose up```

# database and Scrapyd configuration
change values in ```.env``` file

# API:

```/api/apartments``` for all apartments

```/api/apartments/?id={id}``` select 1 apartment

```/api/apartments/filter/?{filter}={value}``` filter apartments

e.g.:

/api/apartments/filter/?water=True&heat=True&petsallowed=True&max_price=1000

## available filters:

### True/False/Int/Value
- city
- forrentbyhousing
- unittype
- agreementtype
- dateavailable
- petsallowed
- furnished
- laundryinunit
- laundryinbuilding
- dishwasher
- fridgefreezer
- airconditioning
- yard
- balcony
- smokingpermitted
- gym
- pool
- concierge
- twentyfourhoursecurity
- bicycleparking
- storagelocker
- elevator
- wheelchairaccessible
- braillelabels
- audioprompts
- barrierfreeentrancesandramps
- visualaids
- accessiblewashroomsinsuite
- hydro
- heat
- water
- cabletv
- internet

### Min Max filters

- posted 
- price
- numberbathrooms
- dateavailable
- numberparkingspots
- areainfeet
