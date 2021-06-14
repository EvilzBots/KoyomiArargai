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

**This Is Anime Inline Section!**
'''

UPDATES_INFO = '''
**Next Inline Updates**:
1. GitHub Extraction
2. Bin Inline Checker
3. Lyrics

**Next Modules Updates**:
1. Global Stats
2. Zipper & UnZipper
'''

@tbot.on(events.callbackquery.CallbackQuery(data="inlinebot"))
async def inlinebot(event):
    await event.edit(IN_TXT, buttons=[
        [Button.switch_inline("✘ Anime ✘", query="anime", same_peer=True), Button.switch_inline("✘ Manga ✘", query="manga", same_peer=True)],
        [Button.inline("Next", data="update_infom")]])

@tbot.on(events.callbackquery.CallbackQuery(data="update_infom"))
async def update_infom(event):
   await event.answer(UPDATES_INFO, show_alert= True)
