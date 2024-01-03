from telethon import TelegramClient, events
from telethon.tl.custom.button import Button
from . import *
from os import getenv
import asyncio

api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")


bot = TelegramClient(
    'Bot',
    api_id=api_id,
    api_hash=api_hash

).start(
    bot_token=bot_token

)

async def getMe(bot):
    global bot_username
    bot_user = await bot.get_me()
    bot_username = bot_user.username

@bot.on(events.NewMessage(pattern='/start'))
async def do(event):
    if event.is_private:
        await event.respond(
            wlcm_msg,
            parse_mode = "md",
            buttons=Button.url(
                btn_txt,
                url=f"https://t.me/{bot_username}?startgroup=true"
            )
        )

@bot.on(events.NewMessage(pattern=censored))
async def do(event):
    if not event.is_private:
        await event.delete()
        del_msg = await event.respond(censr_msg)
        await asyncio.sleep(10)
        await del_msg.delete()