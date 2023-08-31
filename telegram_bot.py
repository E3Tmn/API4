import telegram
from dotenv import load_dotenv
import time
import os
import random
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.environ["PATH_TO_FOLDER"])
    parser.add_argument('--seconds', default=14400, type=int)
    args = parser.parse_args()
    bot = telegram.Bot(os.environ['TELEGRAM_TOKEN'])
    while True:
        for root, dirs, files in os.walk(args.path):
            try:
                with open(os.path.join(root, random.choice(files)), 'rb') as file:
                    bot.send_document(os.environ['TG_CHAT_ID'], document=file)
                time.sleep(args.seconds)
            except telegram.error.NetworkError:
                print("network error")
                break


if __name__ == "__main__":
    main()
