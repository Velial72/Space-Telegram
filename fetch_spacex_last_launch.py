import requests
import os
from save_image import save_image


def fetch_spacex_last_launch(entered_values):
    api_space = f'https://api.spacexdata.com/v5/launches/{entered_values}'
    filename = 'space'
    folder_path = os.path.join('images')

    response = requests.get(api_space, timeout=60)
    response.raise_for_status()

    os.makedirs('images', exist_ok=True)
    images = response.json()['links']['flickr']['original']

    for url_image in images:
        name_count = len(os.listdir(folder_path))
        save_image(url_image, folder_path, filename, name_count)
