from save_image import *
from dotenv import load_dotenv


def fetch_nasa_apod():
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    filename = 'nasa'
    folder_path = os.path.join('images')
    payload = {"api_key": token}
    name_count = len(os.listdir(folder_path))

    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()

    if os.path.exists('images/'):
        pass
    else:
        os.mkdir('images')

    if checking_the_extension(response.json()['url']) == '.jpg':
        save_image(response.json()['url'], folder_path, filename, name_count)


fetch_nasa_apod()
