import re
import random
from LaylaRobot import tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

IN_TXT = '''
Here is the help for the Anime Lovers ❤️:
Get information about anime, manga or characters from AniList.
Available commands:
 ➤ `/YONE` <anime>: returns information about the anime.
'''
@Evil.on(events.callbackquery.CallbackQuery(data="inlinebot"))
async def inlinebot(event):
    await event.edit(IN_TXT)
