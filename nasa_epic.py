import requests
from download import download_a_picture
from dotenv import load_dotenv
import datetime
import os
import argparse


def fetch_archive_picture(day, i, dates):
    if len(dates) > 0:
        payload = {
            'api_key': os.environ['NASA_API_KEY'],
        }
        nasa_epic_url = 'https://api.nasa.gov/EPIC/archive/natural/'
        response_nasa2_url = requests.get(f'{nasa_epic_url}{day.strftime("%Y/%m/%d") }/png/{dates[0]["image"]}.png', params=payload)
        response_nasa2_url.raise_for_status()
        download_a_picture(response_nasa2_url.url, 'nasa_epic', i)


def fetch_nasa_epic_picture(count):
    payload = {
        'api_key': os.environ['NASA_API_KEY'],
    }
    nasa_date_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    today = datetime.date.today()
    for i in range(count):
        day = today - datetime.timedelta(days=i)
        response_date = requests.get(f'{nasa_date_url}{day.strftime("%Y-%m-%d")}', params=payload)
        response_date.raise_for_status()
        dates = response_date.json()
        fetch_archive_picture(day, i, dates)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default=20)
    args = parser.parse_args()
    fetch_nasa_epic_picture(args.count)
