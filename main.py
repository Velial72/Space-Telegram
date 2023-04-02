from dotenv import load_dotenv
import argparse
import os
import telegram
import random
import time


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Введите: ID канала телеграм и частоту публикаций в секундах')
    parser.add_argument('rate', nargs='?', type=int, help='частота публикаций', default='14400')
    entered_values = parser.parse_args()
    while True:
        try:
            token = os.environ['TG_TOKEN']
            chat_id = os.environ['CHAT_ID']
            folder_path = os.path.join('images')
            bot = telegram.Bot(token=token)
            tree = os.walk('images')
            
            for root, catalog, images in tree:
                for image in images:
                    path_to_image = os.path.join(root, image)
                    with open(path_to_image, 'rb') as file:
                        bot.send_document(chat_id=chat_id, document=file, timeout=60)
                        time.sleep(entered_values.rate)
                random.shuffle(images)
                telegram.error.NetworkError()
        except Exception as error:
            logging.error(error)
            time.sleep(5)
