import requests
import os
import urllib


def save_image(url, path, filename, name_count):
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join(path, f'{filename}_{name_count}.jpg'), 'wb') as file:
        file.write(response.content)


def checking_the_extension(url):
    extension = os.path.splitext((urllib.parse.urlsplit(url)[2]))[1]
    return extension
