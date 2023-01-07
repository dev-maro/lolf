import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX.misc import SUDOERS
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
                        
@app.on_message(
    command(["/command_sudo", "/command"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اهلا عزيزي المطور\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["سورس"],
                        ["الاوامر","الاحصائيات"],
                        ["المحظورين عام","مطور البوت"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
       await message.reply_text(
                "اهلا عزيزي العضو\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["سورس"],
                        ["الاوامر","الالعاب"],          
                    ],
                    resize_keyboard=True
                )
            )     


@app.on_message(
    command(["الاوامر"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اليك اوامر البوت عزيزي المطور",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","اوامر 4"],
                        ["اوامر 5","اوامر 6"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
       await message.reply_text(
                "اليك اوامر البوت عزيزي العضو",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","اوامر 4"],
                        ["اوامر 5"],
                    ],
                    resize_keyboard=True
                )
            )                 
