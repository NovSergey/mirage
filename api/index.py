import asyncio
import threading

from fastapi import FastAPI

from tgbot.main import start_bot


app = FastAPI()

def start_bot_f():
    asyncio.run(start_bot())

@app.get('/start')
async def start():
    bot_process = multiprocessing.Process(target=start_bot_f, daemon=True)
    bot_process.start()
    return 'started'

@app.get("/")
def index():
    return "ok"
