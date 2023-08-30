import requests
from download import download_a_picture
from dotenv import load_dotenv
import datetime
import os
import argparse


def fetch_archive_picture(day, number_of_picture, dates, NASA_API_KEY):
    payload = {
        'api_key': NASA_API_KEY,
    }
    nasa_epic_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    response_nasa = requests.get(f'{nasa_epic_url}{day.strftime("%Y/%m/%d") }/png/{dates[0]["image"]}.png', params=payload)
    response_nasa.raise_for_status()
    download_a_picture(response_nasa.url, 'nasa_epic', number_of_picture)


def fetch_nasa_epic_picture(count, NASA_API_KEY):
    payload = {
        'api_key': NASA_API_KEY,
    }
    nasa_date_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    today = datetime.date.today()
    for number in range(count):
        day = today - datetime.timedelta(days=i)
        response_date = requests.get(f'{nasa_date_url}{day.strftime("%Y-%m-%d")}', params=payload)
        response_date.raise_for_status()
        dates = response_date.json()
        if dates:
            fetch_archive_picture(day, number, dates, NASA_API_KEY)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default=20)
    args = parser.parse_args()
    NASA_API_KEY = os.environ['NASA_API_KEY']
    fetch_nasa_epic_picture(args.count, NASA_API_KEY)


if __name__ == "__main__":
    main()