import re
import os
import random
from LaylaRobot import telethn as tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

ABOUT_TXT = '''
**@MrKoyomiBot Is Online Since 16 June 2021!**

`He is an anime themed group managemer bot , with lots
of features, modules & plugins that can make easy to 
manage your group with little mixture of happiness, fun, Love.`

✨ Update Channel : @KoyomiUpdates
✨ Support Group : @KoyomiSupport 
'''

@tbot.on(events.callbackquery.CallbackQuery(data="aboutme"))
async def aboutme(event):
    await event.edit(ABOUT_TXT, buttons=[
        [Button.inline("My Devs 🥀 ", data= "devs")]])

DEV_TXT = '''
**I Am Inspired By The Original Work Done By**
**@PaulSonofLars For Marie.!**
**@Sawada For SaitamaRobot!**
**Dan For His Pyrogram Library**
**Lonami For Telethon Library**

**My Inspired Developer:**

**1. @I_A_M_E_V_I_L [ Noob ]**
**2. @MaskedVirus [My Pro Sir]**
**3. @TheStarkxD [My Pro Friend]**

**~ Thanks**
'''

@tbot.on(events.callbackquery.CallbackQuery(data="devs"))
async def devs(event):
    await event.edit(DEV_TXT, buttons=[[Button.inline("Back", data="source_back")]])
