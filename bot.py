import asyncio
import uvicorn
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types, F
import logging

API_TOKEN = '7327562948:AAGiH_qsu4Uh5816u2F26Y6ifOgxPu9QPdc'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

app = FastAPI()


@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling(bot)

async def start_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8090)
    server = uvicorn.Server(config)
    await server.serve()

async def inactive():
    while True:
        print("ok")
        await asyncio.sleep(40)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.create_task(start_server())
    loop.create_task(start_bot())
    loop.create_task(inactive())
    loop.run_forever()
