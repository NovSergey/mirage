import asyncio

from flask import Flask

from tgbot.main import start_bot


app = Flask(__name__)

@app.get("/start_bot")
def start_bot():
    loop = asyncio.new_event_loop()
    loop.create_task(start_bot())
    loop.run_forever()
    return "ok"
