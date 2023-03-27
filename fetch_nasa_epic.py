import os
from save_image import save_image
import requests
import datetime


def fetch_nasa_epic(token):
    filename = 'epic'
    payload = {"api_key": token}
    folder_path = os.path.join('images')
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/image', params=payload, timeout=60)
    os.makedirs('images', exist_ok=True)

    today = datetime.date.today()
    date_of_image = today - datetime.timedelta(days=1)
    formatted_date = date_of_image.strftime("%Y/%m/%d")
    for name_image in response.json():
        name_count = len(os.listdir(folder_path))
        info_image = name_image['image']

        api_epic = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{info_image}.png',
                                params=payload)
        endpoint = api_epic.url

        save_image(endpoint, folder_path, filename, name_count)
