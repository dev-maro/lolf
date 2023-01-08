import asyncio
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS, OWNER
from AnonX.utils.database import add_sudo, remove_sudo


import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OW = getenv("OW", "5768130077")

DEVSOURCE = list(map(int, getenv("DEVSOURCE", "5768130077").split()))



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
    command(["رتبتي"])
    & filters.group
    & ~filters.edited
)
async def rotba(client: Client, message: Message):
    if message.from_user.id in DEVSOURCE:
        await message.reply_text("✵ رتبتك هي : مطور السورس 🌚")
    elif message.from_user.id in SUDOERS:
        await message.reply_text("✵ رتبتك هي : المطور ❤")        
    else:
        await message.reply_text("✵ رتبتك هي : العضو المسكين 🥹")
        
@app.on_message(
    command(["رتبته"])
    & ~filters.edited
)
async def rotba1(client: Client, message: Message):
    if message.reply_to_message.from_user.id in DEVSOURCE:
        await message.reply_text("✵ رتبته هي : مطور السورس 🌚")
    elif message.reply_to_message.from_user.id in SUDOERS:
        await message.reply_text("✵ رتيته هي : المطور ❤")        
    else:
        await message.reply_text("✵ رتبته هي : العضو المسكين 🥹")        


@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
async def anamean(client: Client, message: Message):
    if message.from_user.id in DEVSOURCE:
        await message.reply_text("✵ انت اسلام مطور السورس 🙈")
    elif message.from_user.id in SUDOERS:
        await message.reply_text("✵ انت مطوري 🥹")        
    else:
        await message.reply_text("انت عضو بائس 😭")
        
@app.on_message(
    command(["انت مين"])
    & filters.group
    & ~filters.edited
)
async def anamean1(client: Client, message: Message):
    if message.reply_to_message.from_user.id in DEVSOURCE:
        await message.reply_text("✵ انت اسلام مطور السورس 🙈")
    elif message.reply_to_message.from_user.id in SUDOERS:
        await message.reply_text("✵ انت مطوري 🥹")        
    else:
        await message.reply_text("انت عضو بائس 😭")

@app.on_message(
    command(["بوت"])
    & filters.group
    & ~filters.edited
)
async def rotba(client: Client, message: Message):
    if message.from_user.id in DEVSOURCE:
        await message.reply_text("اوامرك يا مبرمج اسلام 💕")
    if message.from_user.id in OWNER:
        await message.reply_text("مطوري كيف حالك")        
    elif message.from_user.id in SUDOERS:
        await message.reply_text("اتفضل يا مطور الثانوي ماذا تريد")        
    else:
        await message.reply_text("العضو الغلبان عايز اي 😂")