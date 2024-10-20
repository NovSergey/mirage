from fastapi import FastAPI

from tgbot.main import bot, dp


app = FastAPI()

@app.get('/start')
async def start():
    await dp.start_polling(bot)
    return ''

@app.get("/")
def index():
    return "ok"
