import telegram
from dotenv import load_dotenv
import time
import os
import random
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа позволяет выбрать картинку, которая будет опубликована в телеграм канале'
    )
    parser.add_argument('--path', default=os.environ["PATH_TO_FOLDER"], help='Путь до картинки')
    parser.add_argument('--seconds', default=14400, type=int, help='Частота публикаций картинок')
    parser.add_argument('--filename', help='Название картинки')
    args = parser.parse_args()
    bot = telegram.Bot(os.environ['TELEGRAM_TOKEN'])
    infinity = True
    delay = 1
    while infinity:
        for root, dirs, files in os.walk(args.path):
            time.sleep(delay)
            if args.filename:
                filename = args.filename
                infinity = False
            else:
                filename = random.choice(files)
            with open(os.path.join(root, filename), 'rb') as file:
                try:
                    bot.send_document(os.environ['TG_CHAT_ID'], document=file)
                    delay = args.seconds
                except telegram.error.NetworkError:
                    print("network error")
                    delay = 60
                    break


if __name__ == "__main__":
    main()
