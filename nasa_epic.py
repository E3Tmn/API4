import requests
from download import download_a_picture
from dotenv import load_dotenv
import datetime
import os
import argparse


def fetch_nasa_epic_picture(count):
    load_dotenv()
    payload = {
        'api_key': os.environ['DEMO_KEY'],
        }
    nasa_date_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    today = datetime.date.today()
    for i in range(int(count) if count else 20):
        day = today - datetime.timedelta(days=i)
        response_date = requests.get(f'{nasa_date_url}{day.strftime("%Y-%m-%d")}', params=payload)
        response_date.raise_for_status()
        dates = response_date.json()
        if len(dates) > 0:
            response_nasa2_url = requests.get(f'{nasa_epic_url}{day.strftime("%Y/%m/%d") }/png/{dates[0]["image"]}.png', params=payload)
            download_a_picture(response_nasa2_url.url, 'nasa_epic', i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default="")
    args = parser.parse_args()
    try:
        fetch_nasa_epic_picture(args.count)
    except requests.exceptions.HTTPError as err:
        print(err)
