import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سورس البوب","المطورين","مطورين السورس","مطورين "])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f698f60484b7aef0d6f29.jpg",
        caption=f"""**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين البوب ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑀𝐴𝑅𝑂 ", url=f"https://t.me/j_s_9"), 
                 ],[
                    InlineKeyboardButton(
                        "𝐴𝐿𝑃𝑂𝑃", url=f"https://t.me/vip_alpop"),
                ],[
                    InlineKeyboardButton(
                        "𝐶𝑂𝑀𝑀𝐔𝑁𝐼𝐶𝐴𝑇𝐼𝑂𝑁", url=f"https://t.me/O_U_O_BOT"),
                    InlineKeyboardButton(
                        "𝐺𝑅𝑂𝐔𝑃", url=f"https://t.me/bar_alpop"),
                ],[
                
                    InlineKeyboardButton(
                        "𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊", url=f"https://t.me/source_alpop"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["ماروو","مارووو","الملك","مبرمج","maro","مارو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("j_s_9")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺\n\n‍ ¦namee :{name}\n ¦u𝘴e𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥo :{usr.bio}\n\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["البوب","امير","المبرمج","alpop","مبرمج السورس","مطور السورس","باشا مصر"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("vip_alpop")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺\n\n¦namee :{name}\n ¦u𝘴e𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥo :{usr.bio}\n\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["التسليه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("source_alpop")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺\n\n‍ ★¦ اوامر التسليه ( الرفع ) \n\n ★¦ رفع نمله+تنزيل نمله \n\n ★¦ رفع صرصار+تنزيل صرصار \n\n ★¦ رفع رقاصه+تنزيل رقاصه \n\n رفع متناك+تنزيل متناك \n\n ★¦ رفع نجس+تنزيل نجس  \n\n ★¦رفع عره+تنزيل عره \n\n ★¦ رفع بقره+تنزيل بقره \n\n ★¦ رفع قرد+تنزيل قرد \n\n ★¦ رفع قلبي+تنزيل قلبي \n\n ★¦رفع خدام+تنزيل خدام \n\n ★¦ رفع عرص+تنزيل عرص \n\n ★¦ رفع ارمله+تنزيل ارمله \n\n ★¦ رفع مزه+تنزيل مزه \n\n ★¦رفع ابني+تنزيل ابني  \n\n ★¦ رفع خاينه+تنزيل خاينه \n\n ★¦ رفع بنتي+تنزيل بنتي \n\n ★¦ رفع خاين+تنزيل خاين \n\n ★¦ رفع خول+تنزيل خول \n\n ★¦ رفع حمار+تنزيل حمار \n\n ★¦ رفع غبي+تنزيل غبي  \n\n ★¦ رفع مراتي+تنزيل مراتي  \n\n ★¦ رفع زبال+تنزيل زبال \n\n ★¦ رفع خدامه+تنزيل خدامه \n\n ★¦ رفع كلبه+تنزيل كلبه\n\n ★¦ رفع اخويا+تنزيل اخويا  \n\n ★¦ رفع حرامي+تنزيل حرامي \n\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["هديه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("source_alpop")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺\n\n دا بقا يباشا اسم الاكس الكسرت قلبي الله يحرقها يارب\n\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f698f60484b7aef0d6f29.jpg",
        caption=f"""**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس البوب\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐴𝐿𝑃𝑂𝑃", url=f"https://t.me/vip_alpop"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊", url=f"https://t.me/source_alpop"),
                ],

            ]

        ),

    )
