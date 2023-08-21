import telegram
from dotenv import load_dotenv
import os


load_dotenv()
TG_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telegram.Bot(TG_TOKEN)
bot.send_message(chat_id="@NASA_AND_SPASE_X", text="Тестировочка")
print(bot.get_me())