import asyncio
from threading import Thread

import requests
from flask import Flask
from aiogram import Bot, Dispatcher, types, F
import logging

API_TOKEN = '7327562948:AAE6xyoci6axfKk-bUK4yHHGig_PCPu3FS4'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.get("/")
def index():
    return "ok"

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling(bot)

async def inactive():
    while True:
        await asyncio.sleep(40)
        requests.get("http://0.0.0.0:8090")

def start_server():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = Thread(target=start_server)
    t.start()
    loop = asyncio.new_event_loop()
    loop.create_task(start_bot())
    loop.create_task(inactive())
    loop.run_forever()
