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

• This Is Anime Section! •
'''
@tbot.on(events.callbackquery.CallbackQuery(data="inlinebot"))
async def inlinebot(event):
    await event.edit(IN_TXT, buttons=[
        [Button.switch_inline("✘ Anime ✘ ", query="anime", same_peer=True), Button.switch_inline("✘ Manga ✘", query="manga", same_peer=True)],
        [Button.switch_inline("✘ Character Info ✘", query="character", same_peer=True)],
        [Button.inline("Next »", data = "search_inline")]]
