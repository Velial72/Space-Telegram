from dotenv import load_dotenv
import argparse
import os
import telegram
import random
import time


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Введите: ID канала телеграм')
    parser.add_argument('telegram_id', nargs='?', help='ID канала', default='@space464')
    entered_values = parser.parse_args()
    while True:
        token = os.environ('TG_TOKEN')
        rate = os.getenv('RATE_OF_PUBLICATION')
        folder_path = os.path.join('images')
        bot = telegram.Bot(token=token)
        tree = os.walk('images')

        for root, catalog, images in tree:
            for image in images:
                path_to_image = os.path.join(root, image)
                with open(path_to_image, 'rb') as file:
                    bot.send_document(chat_id=entered_values.telegram_id, document=(file), timeout=60)
                time.sleep(int(rate))
            random.shuffle(images)
