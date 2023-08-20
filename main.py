import requests
import os
from urllib.parse import urlparse
import datetime


def fetch_file_extension(url):
    return(os.path.splitext(urlparse(url).path)[1])


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


def fetch_nasa_epic_picture():
    payload = {
        'api_key': 'DEMO_KEY',
        }
    nasa_date_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    today = datetime.date.today()
    for i in range(50):
        day = today - datetime.timedelta(days=i)
        response_date = requests.get(f'{nasa_date_url}{day.strftime("%Y-%m-%d")}', params=payload)
        response_date.raise_for_status()
        if len(response_date.json()) > 0:
            response_nasa2_url = requests.get(f'{nasa_epic_url}{day.strftime("%Y/%m/%d") }/png/{response_date.json()[0]["image"]}.png', params=payload)
            download_a_picture(response_nasa2_url.url, 'nasa_epic', i)


def fetch_spacex_launch():
    num_of_picture = 0
    spacex_url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(spacex_url)
    response.raise_for_status()
    for link_to_the_picture in response.json()[30]['links']['flickr']['original']:
        num_of_picture += 1
        download_a_picture(link_to_the_picture, 'spacex_images', num_of_picture)


def download_a_picture(url, path, number):
    response = requests.get(url)
    response.raise_for_status()
    if not os.path.isdir(f"{path}"):
        os.mkdir(f"{path}")
    with open(f'{path}/image_{number}{fetch_file_extension(url)}', 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    # fetch_spacex_launch()
    # fetch_nasa_apod_picture()
    fetch_nasa_epic_picture()
