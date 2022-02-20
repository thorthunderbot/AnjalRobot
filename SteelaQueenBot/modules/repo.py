import os
import re
from telethon import events, Button
from telegram.parsemode import ParseMode

ANJAL_PIC = "https://telegra.ph/file/f1603e71bdc0b60082609.jpg"

@register(pattern=("/repo"))
async def repo(e):
    k = f"**Hi** {e.sender.first_name} **Thank You For Using Here is My Current Repo **"
    BUTTON = [
        [
            Button.url("Repo", "https://github.com/godofanjal/AnjalRobot"),
            Button.url("Owner", "https://telegram.me/call_me_crazyboy"),
        ]
    ]
    await cray.send_file(
        e.chat_id,
        file=(ANJAL_PIC),
        caption=k,
        parse_mode=ParseMode.HTML,
        buttons=BUTTON,
        reply_to=e,
    )
