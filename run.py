import telegram
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

myToken = os.environ['TELEGRAM_TOKEN']
myChatId = os.environ['TELEGRAM_CHAT_ID']


async def send(msg, chat_id, token=myToken):
    bot = telegram.Bot(token=token)
    await bot.send_photo(chat_id=chat_id, photo=open('./alert.png', 'rb'))
    print('Message Sent!')


if __name__ == "__main__":
    MessageString = 'Testing from virtual server'
    print(MessageString)
    asyncio.run(send(msg=MessageString, chat_id=myChatId, token=myToken))