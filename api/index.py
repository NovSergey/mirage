from fastapi import FastAPI

from tgbot.main import start_bot


app = FastAPI()


@app.get('/start')
async def start():
    await start_bot()
    return ''

@app.get("/")
def index():
    return "ok"
