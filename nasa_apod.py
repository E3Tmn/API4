import requests
import argparse
import os
from download import download_a_picture
from dotenv import load_dotenv


def fetch_nasa_apod_picture(count, NASA_API_KEY):
    payload = {
        'api_key': NASA_API_KEY,
        'count': count
        }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for num_of_picture, dictionary in enumerate(response.json()):
        if dictionary['media_type'] == 'image':
            download_a_picture(dictionary['hdurl'], 'nasa_images', num_of_picture)


def main():
    load_dotenv()
    NASA_API_KEY = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default="50")
    args = parser.parse_args()
    fetch_nasa_apod_picture(args.count, NASA_API_KEY)


if __name__ == "__main__":
   main()

