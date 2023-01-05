#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/AnonXBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/AnonXBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
from datetime import datetime, timedelta
from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from strings.filters import command

import config
from config import adminlist, chatstats, clean, userstats
from strings import get_command
from AnonX import app, userbot
from AnonX.misc import SUDOERS
from AnonX.utils.database import (get_active_chats,
                                       get_authuser_names, get_client,
                                       get_particular_top,
                                       get_served_chats,
                                       get_served_users, get_user_top,
                                       is_cleanmode_on, set_queries,
                                       update_particular_top,
                                       update_user_top)
from AnonX.utils.decorators.language import language
from AnonX.utils.formatters import alpha_to_int

BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")



@app.on_message(command(["/pin", "ثبت"]) & filters.user(OWNER_ID))
@language
async def braodcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_5"])
        query = message.text.split(None, 1)[1]
        if "-pin" or "-1" in query:
            query = query.replace("-pin", "-1")
        if "-nobot" in query:
            query = query.replace("-nobot", "-5")
        if "-pinloud" or "-5" in query:
            query = query.replace("-pinloud", "-4")
        if "-assistant" or "-3" in query:
            query = query.replace("-assistant", "-3")
        if "-user" or "-2" in query:
            query = query.replace("-user", "-2")
        if query == "":
            return await message.reply_text(_["broad_6"])

    IS_BROADCASTING = True

    # Bot broadcast inside chats
    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if "-pin" or "-1" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except Exception:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except Exception:
                        continue
                sent += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                continue
        try:
            await message.reply_text(_["broad_1"].format(sent, pin))
        except:
            pass

    # Bot broadcasting to users
    if "-user" or "-2" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text(_["broad_7"].format(susr))
        except:
            pass

    # Bot broadcasting by assistant
    if "-assistant" or "-3" in message.text:
        aw = await message.reply_text(_["broad_2"])
        text = _["broad_3"]
        from AnonX.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.iter_dialogs():
                try:
                    await client.forward_messages(
                        dialog.chat.id, y, x
                    ) if message.reply_to_message else await client.send_message(
                        dialog.chat.id, text=query
                    )
                    sent += 1
                except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except Exception as e:
                    print(e)
                    continue
            text += _["broad_4"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass
    IS_BROADCASTING = False


