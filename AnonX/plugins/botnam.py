import asyncio
import random
from pyrogram.types import InlineKeyboardButton
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from random import choice
from AnonX import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from AnonX.misc import SUDOERS
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

namd = [
f"اسمي {MUSIC_BOT_NAME} يقلب 🙈",
f"عايز اي من {MUSIC_BOT_NAME} 😒",
f"اؤمرني يعيوني 🌚",
f"كل شويه {MUSIC_BOT_NAME} 😭",
f"قلبي ودقاته بينادي علي {MUSIC_BOT_NAME} 🔥🙈",
]

@app.on_message(
    command(["بوت"])
    & ~filters.edited
)
async def mreslam(client: Client, message: Message):
    barr = random.choice(namd) 
    await message.reply_text(barr)
