import importlib
import time
import re
from sys import argv
from typing import Optional
from LaylaRobot.modules import ALL_MODULES
from LaylaRobot.modules.helper_funcs.chat_status import is_user_admin
from LaylaRobot.modules.helper_funcs.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown

IN_START_TEXT = """
*Welcome To Inline Commands Menu:*
"""

buttons = [
    [
        InlineKeyboardButton(
            text="✘ Anime ✘", callback_data="anime_inline"),
    ],

    
    [
        InlineKeyboardButton(text="✘ Help & Commands ✘", callback_data="help_back"),
    ],
]
