import os
from save_image import save_image, get_an_extension
import requests
from dotenv import load_dotenv

def fetch_nasa_apod(token):
    filename = 'nasa'
    folder_path = os.path.join('images')
    os.makedirs('images', exist_ok=True)
    payload = {"api_key": token}
    name_count = len(os.listdir(folder_path))

    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload, timeout=60)
    response.raise_for_status()
    image_url = response.json()['url']
    file_extension = get_an_extension(image_url)

    if file_extension == '.jpg':
        save_image(image_url, folder_path, filename, name_count)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_nasa_apod(token)
