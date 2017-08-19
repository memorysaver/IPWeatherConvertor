import requests


def geocode_by_ip(ip_address):
    response = requests.get(f'http://ipinfo.io/{ip_address}/json')
    loc_json = response.json()
    country = loc_json.get('country', 'unknown')
    city = loc_json.get('city', 'unknown')
    loc = loc_json.get('loc', '0,0').split(',')
    return loc[0], loc[1], country, city
