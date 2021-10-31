import requests
from pprint import pprint


def search_max_intelligence(hero_list):
    result = {'name': '',
              'intelligence': 0}
    uri = 'https://superheroapi.com/api/'
    token = '2619421814940190'
    for hero in hero_list:
        r = requests.get(uri + token + '/search/' + hero)
        if r:
            id = r.json()['results'][0]['id']
            r = requests.get(uri + token + '/' + id + '/powerstats')
            if r:
                if result['intelligence'] <= int(r.json()['intelligence']):
                    result['name'] = hero
                    result['intelligence'] = int(r.json()['intelligence'])
            else:
                print('Response intelligence Failed')
        else:
            print('Response Hero Failed')
    return result


if __name__ == '__main__':
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    pprint(search_max_intelligence(hero_list))
