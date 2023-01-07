
from database import get_db_botname
import random
from datetime import datetime
import requests
from pyrogram import Client
from pyrogram.types import Message
from database import set_db_wait, del_db_botname, get_db_lockreply, set_db_lockreply, del_db_lockreply
from AnonX.misc import SUDOERS








async def namebot(m: Message):
    del_db_botname()
    set_db_wait("namebot", m.from_user.id, m.chat.id)
    await m.reply_text("◍ ارسل لى الاسم الان\n√", reply_to_message_id=m.message_id)


    if m.text == "ضع اسم للبوت":
        if SUDOERS(m):
            await namebot(m)
        else:
            await m.reply_text("✯ انت لست المطور الاساسي\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "namebot"):
            if m.text == "الغاء":
                del_db_wait("namebot")
                await m.reply_text("◍ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("namebot")
            set_db_botname(m.text)
            await m.reply_text("◍ تم تغيير اسم البوت\n√", reply_to_message_id=m.message_id)
            return