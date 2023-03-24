from save_image import *
import argparse
import sys


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(description='Введите ID запуска')
    parser.add_argument('id', nargs='?', help='ID запуска', default='latest')
    launch_id = parser.parse_args(sys.argv[1:])
    api_space = f'https://api.spacexdata.com/v5/launches/{launch_id.id}'
    filename = 'space'
    folder_path = os.path.join('images')

    response = requests.get(api_space)
    response.raise_for_status()
    if os.path.exists('images'):
        pass
    else:
        os.mkdir('images')
    images = response.json()['links']['flickr']['original']
    for url_image in images:
        name_count = len(os.listdir(folder_path))
        save_image(url_image, folder_path, filename, name_count)


fetch_spacex_last_launch()