import os
from datetime import datetime

import requests
import vcr

from .location import geocode_by_ip


def get_weather_data_by_location(**location):
    api_key = os.getenv('DARK_SKY_API_KEY',
                        '580dd9d0eddd4219f6d0f446c7990ec3')
    lat = location.get('lat')
    lng = location.get('lng')
    current = location.get('current').timestamp()
    # Time Machine Request
    url = f'https://api.darksky.net/forecast/{api_key}/'
    url += f'{lat},{lng},{int(current)}'
    url += f'?exclude=minutely,hourly,daily'
    with vcr.use_cassette(f'./weather_api_vcr/{lat}-{lng}-{int(current)}.yml'):
        response = requests.get(url)
    if response.status_code != 200:
        return {}
    return response.json()


def get_weather_data(**kwargs):
    ip_address = kwargs.get('ip_address')
    date_str = kwargs.get('date_string')
    lat, lng, country, city = geocode_by_ip(ip_address)
    current = datetime.strptime(f'{date_str} -0500', '%m/%d/%y %H:%M %z')
    result = get_weather_data_by_location(lat=lat, lng=lng, current=current)
    return result
