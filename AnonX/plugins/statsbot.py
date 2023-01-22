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

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


              
@app.on_message(
    command(["الاحصائيات", "احصائيات"])
    & filters.user(OWNER_ID)
    & ~filters.edited
)
async def selff(client: Client, message: Message):
    usr = await client.get_users(BOT_ID)
    name = usr.first_name
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    async for photo in client.iter_profile_photos(BOT_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""مرحبا بك يا مطوري \n\n اليك احصائيات البوت\nالمجموعات: {served_chats}\n\nالمستخدمين{served_users}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘚𝘖𝘜𝘙𝘊𝘌 𝘛𝘈𝘓𝘈 ✘", url=f"https://t.me/GG7GW"),
                ],
            ]
        ),
    )
  
