import re
import os
import random
from LaylaRobot import telethn as tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

N_TXT = '''
**This Next-gen Inline Menu:**
• This Is Anime Section! •
'''
@tbot.on(events.callbackquery.CallbackQuery(data="inlinebot"))
async def extracmds(event):
    await event.edit(N_TXT, buttons=[
           [Button.inline("Cleaner", data="cleaner")]])
