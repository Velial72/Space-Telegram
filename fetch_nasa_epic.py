import os
from save_image import save_image
import requests
import datetime
from dotenv import load_dotenv


def fetch_nasa_epic(payload):
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/image', params=payload, timeout=60)
    response.raise_for_status()
    return response.json()

        
if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    payload = {"api_key": token}
    filename = 'epic'
    folder_path = os.path.join('images')
    os.makedirs('images', exist_ok=True)
    today = datetime.date.today()
    date_of_image = today - datetime.timedelta(days=1)
    formatted_date = date_of_image.strftime("%Y/%m/%d")
    for name_image in fetch_nasa_epic(payload):
        name_count = len(os.listdir(folder_path))
        image_info = name_image['image']
        epic_api = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_info}.png',
                                params=payload)
        epic_api.raise_for_status()
        endpoint = epic_api.url
        save_image(endpoint, folder_path, filename, name_count)
