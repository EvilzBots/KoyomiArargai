import aiohttp
import requests
from LaylaRobot import pbot
from LaylaRobot.modules.anime import (airing_query, anime_query, character_query,
                                   manga_query, shorten, t, url)
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InlineQueryResultPhoto,
                            InputTextMessageContent)


class AioHttp:
    @staticmethod
    async def get_json(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_raw(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.read()

#imported from @LordHitsuki_BOT

@pbot.on_alive_func()
async def alive_func(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(query.id,
                                         results=[
                                             InlineQueryResultPhoto(
                                                 caption="Hey! I have an inline mode, click the buttons below to get inline funcs!",
                                                 photo_url="https://telegra.ph/file/08347ce6b23e35fa2f4de.jpg",
                                                 parse_mode="html",
                                                 title="Need Help?",
                                                 description="Click Here!",
                                                 reply_markup=InlineKeyboardMarkup(
                                                     [[
                                                         InlineKeyboardButton(
                                                             "Aɴɪᴍᴇ", switch_inline_query_current_chat="anime "),
                                                         InlineKeyboardButton(
                                                             "Mᴀɴɢᴀ", switch_inline_query_current_chat="manga")
                                                     ]]
                                                 )
                                             ),
                                         ],
                                         switch_pm_text="Click here to PM",
                                         switch_pm_parameter="start",
                                         cache_time=300
                                         )
