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
        while True:
            with open(os.path.join(root, random.choice(files)), 'rb') as file:
                bot.send_document(os.environ['TG_CHAT_ID'], document=file)
            time.sleep(int(os.environ['FREQ_PUBLISH']))
    
if __name__ == "__main__":
    try:
        main()
    except telegram.error.NetworkError as err:
        print(err)

