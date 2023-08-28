import telegram
from dotenv import load_dotenv
import os
import time
import os
import random
import argparse

def main(path,seconds):
    bot = telegram.Bot(os.environ['TELEGRAM_TOKEN'])
    for root, dirs, files in os.walk(f'{path}'):
        while True:
            try:
                with open(os.path.join(root, random.choice(files)), 'rb') as file:
                    bot.send_document(os.environ['TG_CHAT_ID'], document=file)
                time.sleep(int(seconds))
            except telegram.error.NetworkError as err:
                print("network error")
                break
    
if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.getenv("PATH_TO_FILE"))
    parser.add_argument('--seconds', default=14400)
    args = parser.parse_args()
    main(args.path, args.seconds)
    

