import requests
import os
from urllib.parse import urlparse
import datetime


def fetch_file_extension(url):
    return(os.path.splitext(urlparse(url).path)[1])
    

def fetch_nasa_apod_picture():
    num_of_picture = 0
    payload = {
        'api_key':'DEMO_KEY',
        'count':'50'
        }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url,params=payload)
    response.raise_for_status()
    for dict in response.json():
        if 'hdurl' in dict:
            num_of_picture +=1
            download_a_picture(dict['hdurl'],'nasa_images', num_of_picture)


# def fetch_nasa_epic_picture():
#     payload = {
#         'api_key':'DEMO_KEY',
#         }
    # nasa_url = 'https://api.nasa.gov/EPIC/api/natural/'
    # response = requests.get(nasa_url,params=payload)
    # response.raise_for_status()
    # nasa2_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    # nasa_date = 'https://api.nasa.gov/EPIC/api/natural/date/'
    # today = datetime.date.today()
    # day = today - datetime.timedelta(days=1)
    # formatted_date_1 = day.strftime("%d/%m/%Y")
    # print(formatted_date_1)
    # response = requests.get(f'{nasa_date}{formatted_date_1}',params=payload)
    # print(response.json())
    # for i in range(10):
    #     today = datetime.date.today()
    #     day = today - datetime.timedelta(days=i)
    #     formatted_date_1 = day.strftime("%d/%m/%Y")
    #     print(formatted_date_1)
    #     response = requests.get(f'{nasa2_url}{formatted_date_1}/png/{response.json()[0]["image"]}.png',params=payload)
    #     response.raise_for_status()
    #     if not os.path.isdir(f"nasa_epic"):
    #         os.mkdir(f"nasa_epic")
    #     with open(f'nasa_epic/image_{i}.png', 'wb') as file:
    #         file.write(response.content)


    

def fetch_spacex_launch():
    num_of_picture = 0
    spacex_url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(spacex_url)
    response.raise_for_status()
    for link_to_the_picture in response.json()[30]['links']['flickr']['original']:
        num_of_picture +=1
        download_a_picture(link_to_the_picture,'spacex_images',num_of_picture)
    

def download_a_picture(url,path,number):
    response = requests.get(url)
    response.raise_for_status()
    if not os.path.isdir(f"{path}"):
        os.mkdir(f"{path}")
    with open(f'{path}/image_{number}{fetch_file_extension(url)}', 'wb') as file:
        file.write(response.content) 


if __name__ == "__main__":
    fetch_spacex_launch()
    fetch_nasa_apod_picture()
    # fetch_nasa_epic_picture()