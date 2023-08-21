import requests
import argparse
from download import download_a_picture


def fetch_spacex_launch():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', default="")
    args = parser.parse_args()
    num_of_picture = 0
    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.id}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    if args.id:
        list_of_picture = response.json()['links']['flickr']['original']
    else:
        list_of_picture = response.json()[22]['links']['flickr']['original']
    for link_to_the_picture in list_of_picture:
        num_of_picture += 1
        download_a_picture(link_to_the_picture, 'spacex_images', num_of_picture)


if __name__ == "__main__":
    fetch_spacex_launch()
