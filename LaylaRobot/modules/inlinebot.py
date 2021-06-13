import re
import os
import random
from LaylaRobot import telethn as tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

IN_TXT = '''
**This Next-gen Inline Menu:**
'''
@tbot.on(events.callbackquery.CallbackQuery(data="inlinebot"))
async def inlinebot(event):
    await event.edit(IN_TXT, buttons=[[Button.switch_inline("Anime", query="anime", same_peer=True)]])

