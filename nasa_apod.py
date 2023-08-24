import requests
import argparse
import os
from download import download_a_picture
from dotenv import load_dotenv


def fetch_nasa_apod_picture(count):
    load_dotenv()
    payload = {
        'api_key': os.environ['DEMO_KEY'],
        'count': count if count else 50
        }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for num_of_picture, dict in enumerate(response.json()):
        if dict['media_type'] == 'image':
            download_a_picture(dict['hdurl'], 'nasa_images', num_of_picture)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default="")
    args = parser.parse_args()
    try:
        fetch_nasa_apod_picture(args.count)
    except requests.exceptions.HTTPError as err:
        print(err)
