import requests
from urllib.parse import urlparse
from download import download_a_picture
import datetime


def fetch_nasa_epic_picture():
    payload = {
        'api_key': 'DEMO_KEY',
        }
    nasa_date_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    today = datetime.date.today()
    for i in range(20):
        day = today - datetime.timedelta(days=i)
        response_date = requests.get(f'{nasa_date_url}{day.strftime("%Y-%m-%d")}', params=payload)
        response_date.raise_for_status()
        if len(response_date.json()) > 0:
            response_nasa2_url = requests.get(f'{nasa_epic_url}{day.strftime("%Y/%m/%d") }/png/{response_date.json()[0]["image"]}.png', params=payload)
            download_a_picture(response_nasa2_url.url, 'nasa_epic', i)


if __name__ == "__main__":
    fetch_nasa_epic_picture()
