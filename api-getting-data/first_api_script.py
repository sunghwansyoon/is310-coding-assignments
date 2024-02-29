import apikey
import requests
import json

apikey.save("dpla_key", "a3c1491f37970f0b619f4c3def6bc681")
dpla_api_key = apikey.load("dpla_key")

url = "https://api.dp.la/v2/items?q=kittens&api_key=" + dpla_api_key

response = requests.get(url)
dpla_data = response.json()

# with open("dpla_kittens.json", "w") as json_file:
#     json.dump(response_data, json_file)

print('dataProvider', dpla_data['docs'][0]['dataProvider'])
print('isShownAt', dpla_data['docs'][0]['isShownAt'])
print('sourceResource', dpla_data['docs'][0]['sourceResource'])
print('object', dpla_data['docs'][0]['object'])

from dpla.api import DPLA
dpla = DPLA('your-api-key-here')

# Now make your search
response = dpla.search(q="kittens")
print(response.items[0])