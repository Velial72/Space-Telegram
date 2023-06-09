import requests
import os
from save_image import save_image
import argparse


def fetch_spacex_last_launch(launch_id):
    api_space = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    filename = 'space'
    folder_path = os.path.join('images')

    response = requests.get(api_space, timeout=60)
    response.raise_for_status()

    os.makedirs('images', exist_ok=True)
    images_url = response.json()['links']['flickr']['original']

    for image_url in images_url:
        name_count = len(os.listdir(folder_path))
        save_image(image_url, folder_path, filename, name_count)
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Введите ID последнего запуска')
    parser.add_argument('launch_id', nargs='?', help='ID запуска', default='latest')
    entered_values = parser.parse_args()

    fetch_spacex_last_launch(entered_values.launch_id)
