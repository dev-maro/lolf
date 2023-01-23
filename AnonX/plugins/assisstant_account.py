import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from pyrogram.types import InlineKeyboardButton
from random import choice
import re
from AnonX.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)
import sys
from strings.filters import command
from config import BOT_ID, OWNER_ID
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram import Client, filters


app = Client

load_dotenv()

@app.on_message(
    filters.command("اضف حساب مساعد")
    & filters.user(OWNER_ID)
    & ~filters.edited
)
async def add_new_assisatant(client: Client, message: Message):
    print('hgggggggggggggggg')
