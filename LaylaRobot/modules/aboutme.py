import re
import os
import random
from LaylaRobot import telethn as tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

ABOUT_TXT = '''
🤖 **@MrKoyomiBot is online since 16/June/21 !**

`He is an anime themed group managemer bot , with lots
of features, modules & plugins that can make easy to 
manage your group with little mixture of happiness, fun, Love.`

**✨ Update Channel : @KoyomiUpdates**
**✨ Support Group : @KoyomiSupport**
'''

@tbot.on(events.callbackquery.CallbackQuery(data="aboutme"))
async def aboutme(event):
    await event.edit(ABOUT_TXT, buttons=[
        [Button.inline("Back ", data= "source_back")]])
