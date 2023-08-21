import requests
from urllib.parse import urlparse
import argparse
from download import download_a_picture
from dotenv import load_dotenv


def fetch_nasa_apod_picture():
    num_of_picture = 0
    payload = {
        'api_key': 'DEMO_KEY',
        'count': '50'
        }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for dict in response.json():
        if 'hdurl' in dict:
            num_of_picture += 1
            download_a_picture(dict['hdurl'], 'nasa_images', num_of_picture)


if __name__ == "__main__":
    fetch_nasa_apod_picture()
