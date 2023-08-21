import telegram
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    TG_TOKEN = os.environ['TELEGRAM_TOKEN']
    CHAT_ID = os.environ['CHAT_ID']
    bot = telegram.Bot(TG_TOKEN)
    bot.send_document(CHAT_ID, document=open('nasa_images/image_38.jpg', 'rb'))


if __name__ == "__main__":
    main()
