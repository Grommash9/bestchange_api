import requests
from info_file_downloader import config
import os


def get_file():
    URL = "https://api.bestchange.ru/info.zip"
    response = requests.get(URL, verify=False)

    with open(os.path.join(config.BASE_DIR, 'info.zip'), 'wb') as data_file:
        data_file.write(response.content)
