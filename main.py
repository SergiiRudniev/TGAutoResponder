from pyrogram import Client, filters
from dotenv import load_dotenv
from os import getenv
from Bot import Bot
import config
from CustomFilters import non_bot_non_self

load_dotenv()

api_id = getenv("id")
api_hash = getenv("hash")

app = Client(name="Autoresponder", api_id=api_id, api_hash=api_hash)
bot = Bot(app)

@app.on_message(filters.command("cls", prefixes=">") & filters.me)
async def clear(event, message):
    await bot.Cls(message)

@app.on_message(filters.command("stop", prefixes=">") & filters.me)
async def stop(event, message):
    await bot.Stop(message)


@app.on_message(filters.text & filters.private & filters.create(non_bot_non_self))
async def auto_answer(event, message):
    await bot.OnMessage(message)


app.run()