# Space Telegram

[TODO: скачивание фотографий с сайтов NASA и SpaceX]

### Как установить

Python3 должен быть установлен. Затем используйте 'pip' (или 'pip3' если есть конфликт с Python2) для установки зависимостей:

```pip install -r requiriments.txt```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Пример выполнения программы

запуск ```python3 fetch_nasa_apod.py```

запуск ```fetch_nasa_epic.py```

запуск ```fetch_spacex_last_launch.py -h```

### Настройка окружения

Перед запуском необходимо создать файл `.env` и внести в него переменные:

'NASA_TOKEN' с вашим кодом авторизации на сайте [nasa.gov](https://api.nasa.gov) 

'TG_TOKEN' с вашим токеном телеграмм-бота, обращаться к [BotFather](https://telegram.me/BotFather)

'RATE_OF_PUBLICATION' для установки частоты публикаций (в секундах)

### Цель проекта

Проект написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

