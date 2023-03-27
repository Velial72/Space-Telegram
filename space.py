from fetch_spacex_last_launch import fetch_spacex_last_launch
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Введите ID последнего запуска')
    parser.add_argument('id_launch', nargs='?', help='ID запуска', default='latest')
    entered_values = parser.parse_args()

    fetch_spacex_last_launch(entered_values.id_launch)
