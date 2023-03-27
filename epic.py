from fetch_nasa_epic import fetch_nasa_epic
from dotenv import load_dotenv
import os


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_nasa_epic(token)

