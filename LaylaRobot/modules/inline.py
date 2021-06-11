import html
import re
import os
import requests

from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
from LaylaRobot import telethn as tbot

from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_html

from LaylaRobot import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    INFOPIC,
    dispatcher,
    sw,
)
from LaylaRobot.__main__ import STATS, TOKEN, USER_INFO
import LaylaRobot.modules.sql.userinfo_sql as sql
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from LaylaRobot.modules.sql.global_bans_sql import is_user_gbanned
from LaylaRobot.modules.sql.afk_sql import is_afk, check_afk_status
from LaylaRobot.modules.sql.users_sql import get_user_num_chats
from LaylaRobot.modules.helper_funcs.chat_status import sudo_plus
from LaylaRobot.modules.helper_funcs.extraction import extract_user
from LaylaRobot import telethn as YoneTelethonClient, TIGERS, DRAGONS, DEMONS

app = tbot

@app.on(events.InlineQuery(pattern=r"bin"))
async def hehe(event):
    try:
        input = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        lund = event.builder.article(
           title="Search Something",
           description="You haven't searched anything",
           text="**Bɪɴ Cʜᴇᴄᴋᴇʀ**\nYou haven't given anything to check",
           buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="bin ", same_peer=True)
           )
        await event.answer([lund])
    input = event.text.split(" ", maxsplit=1)[1]
    url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
    res = url.json()
    vendor = res['data']['vendor']
    type = res['data']['type']
    level = res['data']['level']
    bank = res['data']['bank']
    country = res['data']['country']

    me = (await event.client.get_me()).username
    valid = f"""
<b>➤ Valid Bin:</b>
<b>Bin -</b> <code>{input}</code>
<b>Status -</b> <code>Valid Bin</code>
<b>Vendor -</b> <code>{vendor}</code>
<b>Type -</b> <code>{type}</code>
<b>Level -</b> <code>{level}</code>
<b>Bank -</b> <code>{bank}</code>
<b>Country -</b> <code>{country}</code>
<b>Checked By - @{me}</b>
<b>User-ID - {event.sender_id}</b>
"""
    Binning = event.builder.article(
           title="Valid Bin",
           description="It's a valid bin",
           text=valid,
           thumb=InputWebDocument(url="https://telegra.ph/file/0788aaa1b0b48e8e9e2f8.jpg", size=0, mime_type="image/jpeg", attributes=[]),
           parse_mode="HTML",
           buttons=[[Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="bin ", same_peer=True), Button.switch_inline("Sʜᴀʀᴇ", query=f"bin {input}")]
           ])
    await event.answer([Binning])
