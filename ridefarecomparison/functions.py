import requests
import json

def getUberPrice(start_latitude, start_longitude, end_latitude, end_longitude):
    params = {'start_latitude':start_latitude, 'start_longitude': start_longitude, 'end_latitude':end_latitude, 'end_longitude': end_longitude}

    uber_json = requests.get('https://api.uber.com/v1.2/estimates/price', params=params)

    uber_json = json.loads(uber_json.text)
    prices = uber_json['prices']

    uber_keys = ['localized_display_name', 'estimate', 'duration']

    result = []

    for entry in prices:
        price = {}
        for key in uber_keys:
            price[key] = entry[key]
        result.append(price)

    return result
