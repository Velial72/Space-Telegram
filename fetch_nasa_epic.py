import os
from save_image import save_image
import requests
import datetime
from dotenv import load_dotenv


def fetch_nasa_epic(payload):
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{date_of_image}', params=payload, timeout=60)
    response.raise_for_status()
    return response.json()

        
if __name__ == '__main__':
    load_dotenv()
    
    today = datetime.date.today()
    date_of_images = today - datetime.timedelta(days=1)
    formatted_date = date_of_images.strftime("%Y/%m/%d")
    parser = argparse.ArgumentParser(description='Введите дату фотографий')
    parser.add_argument('foto_date', nargs='?', help='дата фото в формате y/m/d', default=formatted_date)
    date_of_foto = parser.parse_args()
    date_of_pictures = date_of_foto.foto_date
    date_of_image = datetime.datetime.strptime(date_of_pictures, '%Y/%m/%d').date()
    
    token = os.environ['NASA_TOKEN']
    payload = {"api_key": token}
    filename = 'epic'
    folder_path = os.path.join('images')
    os.makedirs('images', exist_ok=True)

    for name_image in fetch_nasa_epic(payload):
        name_count = len(os.listdir(folder_path))
        image_info = name_image['image']
        epic_api = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{date_of_pictures}/png/{image_info}.png', params=payload)
        epic_api.raise_for_status()
        endpoint = epic_api.url
        save_image(endpoint, folder_path, filename, name_count)
