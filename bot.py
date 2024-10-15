import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
import logging

API_TOKEN = '7327562948:AAGiH_qsu4Uh5816u2F26Y6ifOgxPu9QPdc'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
