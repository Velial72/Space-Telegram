import requests
import os
import urllib


def save_image(url, path, filename, name_count):
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with open(os.path.join(path, f'{filename}_{name_count}.jpg'), 'wb') as file:
        file.write(response.content)


def check_the_extension(url):

    api_file = urllib.parse.urlsplit(url)[2]
    extension = os.path.splitext(api_file)[1]
    return extension
