import requests
from pprint import pprint


def get_inquiry():
    url = 'https://api.stackexchange.com/2.3/search/'
    params = {"min":"1635379200", "max":"1635552000", "order":"desc", "sort":"activity", "tagged":"python", "site":"stackoverflow"}
    headers = {'Accept': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json()

pprint(get_inquiry())


