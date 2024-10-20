from aiogram import Bot, Dispatcher, types, F
import logging

API_TOKEN = '7327562948:AAG4e1ktQHFFiwZdV34E7e6EEmLCjlVOLdw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling(bot)
