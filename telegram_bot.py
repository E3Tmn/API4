import telegram
from dotenv import load_dotenv
import os
import time
import os
import random


def main():
    load_dotenv()
    bot = telegram.Bot(os.environ['TELEGRAM_TOKEN'])
    for root, dirs, files in os.walk('nasa_images'):
        print(f'{root}{files}')
        while True:
            bot.send_document(os.environ['CHAT_ID'], document=open(f'{root}/{random.choice(files)}', 'rb'))
            time.sleep(int(os.environ['FREQ_PUBLISH']))


if __name__ == "__main__":
    main()
