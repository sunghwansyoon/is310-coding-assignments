import os
import apikey
import requests
import json

def search_channel(username, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,id,statistics",
        "key": api_key,
        "id": id
    }
    response = requests.get(base_url, params=params)
    return response.json()

api_key = apikey.load("google_api_key")
id = "UCs6EwgxKLY9GG4QNUrP5hoQ"
ch_data = search_channel(id, api_key)

data_dir = 'api-getting-data/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

data_file = os.path.join(data_dir, 'my_data.json')
with open(data_file, 'w', encoding='utf-8') as f:
    json.dump(ch_data, f, indent=2)

