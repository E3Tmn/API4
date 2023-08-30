# Выгрузка картинок в телеграм канал
1. Файлы ```nasa_apod.py```, ```nasa_epic.py```, ```spacex_launch.py``` позволяют скачивать фотографии с сайтов [NASA](https://api.nasa.gov/) и [SPACE_X](https://github.com/r-spacex/SpaceX-API).
2. Файл ```download.py``` позволяет скачать картинку по ссылке и сохранить её на компьютер.
3. Файл ```telegram_bot.py``` загружает картинки в телеграм канал

Обратите внимание, что в программы из 1 пункта в конце своей работы ссылаются на функцию ```download_a_picture```, которая написана в файле ```download.py```.
## Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные окружения
Для работы с телеграммом ```telegram_bot.py``` необходимо создать файл ```.env```, записав в него необходимые переменные.
```bash
TELEGRAM_TOKEN = "Уникальный токен от телеграм бота"
TG_CHAT_ID = "Ссылка на телеграм канал"
PATH_TO_FOLDER = 'Путь до файла, где берем фото'
NASA_API_KEY = "Токен сайта"
```
## Запуск
Запуск на Linux(Python 3) или Windows:
```bash
$ python nasa_apod.py 
```
При запуске ```spacex_launch.py``` есть возможность передавать id запуска в качестве параметра. Например:
Запуск на Linux(Python 3) или Windows:
```bash
$ python spacex_launch.py --id 5eb87d46ffd86e000604b388
```
При запуске ```nasa_apod.py``` или ```nasa_epic.py``` есть возможность передавать count - количество фотографий. Например:
Запуск на Linux(Python 3) или Windows:
```bash
$ python spacex_launch.py --count 5
```
