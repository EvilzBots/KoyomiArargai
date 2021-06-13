from LaylaRobot import telethn as tbot
from LaylaRobot.status import *
from telethon import events, Button, types
from ..helpers.search import shorten, anime_query, GRAPHQL
from datetime import timedelta
import requests
import telethon
from telethon.tl.types import BotInlineResult, InputBotInlineMessageMediaAuto, DocumentAttributeImageSize, InputWebDocument, InputBotInlineResult, ChannelParticipantsAdmins
from telethon.tl.functions.messages import SetInlineBotResultsRequest
from ..helpers.other import format_results
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest

@tbot.on(events.InlineQuery(pattern='anime ?(.*)'))
async def inline_anime(event):
    builder = event.builder
    query = event.pattern_match.group(1)
    variables = {'search': query}
    json = requests.post(GRAPHQL, json={'query': anime_query, 'variables': variables}).json()[
        'data'].get('Media', None)
    if json:
        msg, info, trailer, image = format_results(json)
        if trailer:
            buttons =[
                        [
                            Button.url("More Info", url=info),
                            Button.url("Trailer 🎬", url=trailer)
                        ]
                    ]
        else:
            buttons =[
                        [
                            Button.url("More Info", url=info)
                        ]
                    ]
        results = builder.photo(
            file=image,
            text=msg,
            buttons=buttons
        )
        await event.answer([results] if results else None)
