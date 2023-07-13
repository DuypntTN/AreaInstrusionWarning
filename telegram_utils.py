import telegram
import os
from dotenv import load_dotenv

load_dotenv()

myToken = os.environ['TELEGRAM_TOKEN']
myChatId = os.environ['TELEGRAM_CHAT_ID']



async def send_telegram(image_dir):
    print(myToken,myChatId)
    bot = telegram.Bot(token=myToken)
    await bot.send_photo(chat_id=myChatId, photo=open(image_dir, 'rb'))
    print('Message Sent!')

   