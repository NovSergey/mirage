import asyncio
import uvicorn
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
import logging

API_TOKEN = '7327562948:AAGiH_qsu4Uh5816u2F26Y6ifOgxPu9QPdc'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling(bot)

async def start_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.create_task(start_server())
    loop.create_task(start_bot())
    loop.run_forever()
