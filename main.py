from dotenv import load_dotenv
import logging
import argparse
import os
import telegram
import random
import time


def found_path(tree):
    paths_to_pictures = []
    for root, catalog, images in tree:
        for image in images:
            path_to_images = os.path.join(root, image)
            paths_to_pictures.append(path_to_images)
    random.shuffle(paths_to_pictures)
    return paths_to_pictures

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Введите частоту публикаций в секундах')
    parser.add_argument('rate', nargs='?', type=int, help='частота публикаций', default='14400')
    entered_values = parser.parse_args()
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    folder_path = os.path.join('images')
    bot = telegram.Bot(token=token)
    tree = os.walk('images')
    
    while True:
        for path_to_image in found_path(tree):
            with open(path_to_image, 'rb') as file:
                try: 
                    bot.send_document(chat_id=chat_id, document=file, timeout=60)
                    time.sleep(entered_values.rate)
                except telegram.error.NetworkError:
                    logging.error(telegram.error.NetworkError)
                    time.sleep(5)    

                

