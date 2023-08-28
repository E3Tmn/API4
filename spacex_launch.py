import requests
import argparse
from download import download_a_picture


def fetch_spacex_launch(launch_id):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    if launch_id:
        list_of_picture = response.json()['links']['flickr']['original']
    else:
        launch_number = 22
        list_of_picture = response.json()[launch_number]['links']['flickr']['original']
    for num_of_picture, link_to_the_picture in enumerate(list_of_picture):
        download_a_picture(link_to_the_picture, 'spacex_images', num_of_picture)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', default="")
    args = parser.parse_args()
    fetch_spacex_launch(args.id)
 