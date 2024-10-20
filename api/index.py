import asyncio
from threading import Thread

from fastapi import FastAPI

from tgbot.main import start_bot


app = FastAPI()


@app.get('/start')
async def start():
    t = Thread(target=asyncio.run, args=(start_bot(),))
    t.start()
    return ''

@app.get("/")
def index():
    return "ok"
