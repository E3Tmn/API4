import os
import requests
from urllib.parse import urlparse


def fetch_file_extension(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


def download_a_picture(url, path, number):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, f'image_{number}{fetch_file_extension(url)}'), 'wb') as file:
        file.write(response.content)
