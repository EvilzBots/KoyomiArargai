import asyncio
import json
import os
import sys
from random import randint
from sys import version as pyver
from time import ctime, time
from LaylaRobot.modules.fetch import fetch
from motor import version as mongover
from pykeyboard import InlineKeyboard
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent)

keywords_list = [
    "gh_user",
]

async def github_user_func(answers, text):
    URL = f"https://api.github.com/users/{text}"
    result = await fetch(URL)
    buttons = InlineKeyboard(row_width=1)
    buttons.add(
        InlineKeyboardButton(
            text="Open On Github", url=f"https://github.com/{text}"
        )
    )
    caption = f"""
**Info Of {result['name']}**
**Username:** `{text}`
**Bio:** `{result['bio']}`
**Profile Link:** [Here]({result['html_url']})
**Company:** `{result['company']}`
**Created On:** `{result['created_at']}`
**Repositories:** `{result['public_repos']}`
**Blog:** `{result['blog']}`
**Location:** `{result['location']}`
**Followers:** `{result['followers']}`
**Following:** `{result['following']}`"""
    answers.append(
        InlineQueryResultPhoto(
            photo_url=result["avatar_url"],
            caption=caption,
            reply_markup=buttons,
        )
    )
    return answers
