import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX.misc import SUDOERS
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
                        
@app.on_message(
    command(["/command_sudo"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اهلا عزيزي المطور\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["الاحصائيات"],
                        ["اختبار الحساب المساعد","مغادرة الحساب المساعد من المجموعات"],
                        ["تنصيب php البوت"],
                        ["معلومات السيرفر ","بينج السيرفر","قياس سرعة السيرفر"],
                        ["مدة التشغيل","اعادة تشغيل البوت"],
                        ["طريقة الاذاعة","الغاء التوقف"],
                    ],
                    resize_keyboard=True
                )
            )