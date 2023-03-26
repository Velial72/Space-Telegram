from save_image import *
# from dotenv import load_dotenv
import os
import argparse
import sys
from fetch_nasa_epic import fetch_nasa_epic
from fetch_nasa_apod import fetch_nasa_apod
from fetch_spacex_last_launch import fetch_spacex_last_launch


def main():
    parser = argparse.ArgumentParser(description='Введите откуда скачиваем картинки и/или ID последнего запуска')
    parser.add_argument('function', nargs='?', help='название функции', default='all')
    parser.add_argument('id', nargs='?', help='ID запуска', default='latest')
    entered_values = parser.parse_args()

    if entered_values.function == 'fetch_nasa_epic':
        fetch_nasa_epic()
    elif entered_values.function == 'fetch_nasa_apod':
        fetch_nasa_apod()
    elif entered_values.function == 'fetch_spacex_last_launch':
        fetch_spacex_last_launch()
    else:
        fetch_spacex_last_launch()
        fetch_nasa_apod()
        fetch_nasa_epic()


if __name__ == '__main__':
    main()
