import re
import os
import random
from LaylaRobot import telethn as tbot
from telethon import Button
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import KeyboardButtonCallback

ABOUT_TXT = '''
**@MrKoyomiBot Is Online Since 16 June 2021! 

He is an anime themed group managemer bot , with lots
of features, modules & plugins that can make easy to 
manage your group with little mixture of happiness, fun, Love.

If You Wanna Know More About @MrKoyomiBot , Click Below
Options**
'''

@tbot.on(events.callbackquery.CallbackQuery(data="aboutme"))
async def aboutme(event):
    await event.edit(ABOUT_TXT, buttons=[
        [Button.inline("My Devs ❕ ", data= "devs"), Button.inline("Quick Setup ⚙️", data="setup")]])

DEV_TXT = '''
**I Am Inspired By The Original Work Done By**
**@PaulSonofLars For Marie.!**
**@Sawada For SaitamaRobot!**
**Dan For His Pyrogram Library**
**Lonami For Telethon Library**

**My Inspired Developer:**

**1. @I_A_M_E_V_I_L**
**2. @MaskedVirus [ Teacher Of My Developer ]**
**3. @TheStarkxD [ I Thank To My Lovely Friend ]**

**~ Thanks**
'''

@tbot.on(events.callbackquery.CallbackQuery(data="devs"))
async def devs(event):
    await event.edit(DEV_TXT, buttons=[[Button.inline("Main Menu", data="source_back")]])

SETUP_TXT = '''
**⚙️ This Is An Tutorial For Quick Setup :**

**Enable welcome security, soft or strong.
/welcomemute strong
Note: Tries to limit what a user can do when they newly join a group
Strong = Give them 120 seconds to press button, if they fail, kick them off the group
Soft = Restricts them to text only for 24hours after joining**

**Protect accidental contact leakage
/lock contact**

**Stop letting users add bots (Ideally, disable the "Add Users" permission in group settings)
/lock bots**

**Private group? Worried about invite links?
/disable invitelink**

**Lock forwarding stuff into the group
/lock forward**

**Private group? Avoid users kicking themselves by mistake
/disable punchme**

**Users/Spammers flooding non-stop? (Adjust the number to your needs)
/setflood 7
Set what to do when flood control happens using
/setfloodmode mute/ban/tmute
Example: /setfloodmode tmute 15m**

**Don't want some Saitama commands enabled in group?
/listcmds and then use /disable namehere
/listmodules and /disablemodule namehere
Note: if this conflicts with any other bot in group then use /disable@MrKoyomiBot to send that message only to Saitama.**

**Want to auto warn users when they say specific stuff?
See warns > /addwarn command help**

**Don't like some words to be spoken in group? Blacklist them using
/addblacklist word1
word2
"entire sentence here"
Note: You can use "quotes for" if there is a sentence and not a word.**

**Don't want to explain to each newbie? Setup rules!
/setrules
 Awesome Rules here**

**Don't want our awesome random welcome messages? Use a custom one using
/setwelcome Hi, welcome to my group
Note: This command has more stuff you can use, see /welcomehelp first.**

**Have multiple groups to handle? Setup Federations!
Read help for this, this has a bit of a learning curve.**

**Enable reporting so that your users can report troublemakers to admins.
/reports on
Note: Send in group to enable group reports and send in Saitama's pm so that he will report any enabled group to Your pm.**

**Want to track which of your admins did what? Who banned who? Who joined?
Setup a log channel, see help for instructions.**


**Lastly, most of these would apply to almost any Saitama like bot, please do spread the word around for basic chat control and protect yourself from spammers/scammers and troublemakers.**

**Need help? Come visit us at @KoyomiSupport**

**~ Thanks Sawada**
'''

@tbot.on(events.callbackquery.CallbackQuery(data="setup"))
async def setup(event):
    await event.edit(SETUP_TXT, buttons=[[Button.inline("Main Menu", data="source_back")]])
