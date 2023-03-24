from dotenv import load_dotenv
from fetch_spacex_last_launch import *
from fetch_nasa_apod import *
from fetch_nasa_epic import *


def main():
    load_dotenv()
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epic()


if __name__ == '__main__':
    main()
