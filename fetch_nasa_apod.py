import os
from save_image import save_image, check_the_extension
import requests


def fetch_nasa_apod(token):
    filename = 'nasa'
    folder_path = os.path.join('images')
    payload = {"api_key": token}
    name_count = len(os.listdir(folder_path))

    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload, timeout=60)
    response.raise_for_status()
    os.makedirs('images', exist_ok=True)
    file_extension = get_an_extension(response.json()['url'])

    if file_extension == '.jpg':
        save_image(response.json()['url'], folder_path, filename, name_count)

