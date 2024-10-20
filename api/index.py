import asyncio
import threading

from fastapi import FastAPI

from tgbot.main import start_bot


app = FastAPI()


@app.get('/start')
async def start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot_thread = threading.Thread(target=loop.run_until_complete, args=(start_bot(),), daemon=True)
    bot_thread.start()
    return 'started'

@app.get("/")
def index():
    return "ok"
