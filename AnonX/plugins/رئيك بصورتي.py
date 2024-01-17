import asyncio
from pyrogram import Client, filters
from random import choice
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from AnonX import app
from typing import Union
from pyrogram.types import InlineKeyboardButton

RAEAK = ["زينه","حلوه","فخمه","جميله","خوش","انيقه","مو حلوه","بشعه","مو زينه","كلش حلوه","استمر بيها","احبها","غيرها حباب"]

@app.on_message(
    command(["رأيك","رئيك بصورتي","شون صورتي","رايك بصورتي"])
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""صورتك {choice(RAEAK)} 🧸♥️""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
