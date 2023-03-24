import telegram
from dotenv import load_dotenv
import os
import random
import time

while True:
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    rate = os.getenv('RATE_OF_PUBLICATION')
    folder_path = os.path.join('images')
    bot = telegram.Bot(token=token)
    tree = os.walk('images')

    for root, catalog, images in tree:
        for image in images:
            bot.send_document(chat_id='@space464', document=open(f'{folder_path}/{image}', 'rb'), timeout=60)
            time.sleep(int(rate))
        random.shuffle(images)
