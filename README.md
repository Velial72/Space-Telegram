# Space Telegram

[TODO: скачивание фотографий с сайтов NASA и SpaceX]

### Как установить

Python3 должен быть установлен. Затем используйте 'pip' (или 'pip3' если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requiriments.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Пример выполнения программы

запуск 
```
python3 apod.py
```

запуск 
```
fetch_epic.py
```

запуск 
```
space.py -h
```

запуск 
```
main.py
```

### Настройка окружения

Перед запуском необходимо создать файл `.env` и внести в него переменные:

`NASA_TOKEN` с вашим кодом авторизации на сайте [nasa.gov](https://api.nasa.gov) 

`TG_TOKEN` с вашим токеном телеграмм-бота, обращаться к [BotFather](https://telegram.me/BotFather)

### Цель проекта

Проект написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

