from pprint import pprint
import os
import requests
import yadisk


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': os.path.basename(file_path), 'overwrite': True}
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        response = requests.get(url, params=params, headers=headers)
        href = response.json()['href']
        upload = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу: ')
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
