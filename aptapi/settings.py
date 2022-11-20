import os

DB_USER = os.environ.get('POSTGRES_USER', '')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
DB_NAME = os.environ.get('POSTGRES_DB', '')
HOST = 'postgres'
DB_PORT = 5432


apt_unit_attributes_1 = {'city', 'forrentbyhousing', 'unittype',
 'agreementtype', 'dateavailable', 'petsallowed', 'furnished', 'laundryinunit',
 'laundryinbuilding', 'dishwasher', 'fridgefreezer', 'airconditioning', 'yard', 'balcony',
 'smokingpermitted', 'gym', 'pool', 'concierge', 'twentyfourhoursecurity',
 'bicycleparking', 'storagelocker', 'elevator', 'wheelchairaccessible', 'braillelabels',
 'audioprompts', 'barrierfreeentrancesandramps', 'visualaids', 'accessiblewashroomsinsuite',
 'hydro', 'heat', 'water', 'cabletv', 'internet'}

apt_unit_attributes_2 = {'posted', 'price', 'numberbedrooms', 'numberbathrooms', 'dateavailable',
                          'numberparkingspots', 'areainfeet'}
