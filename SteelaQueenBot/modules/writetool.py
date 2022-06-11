from pyrogram import filters

from SteelaQueenBot import pbot


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Give some text to write...")
    m = await message.reply_text("» I writing please wait...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("» Uploading...")
    await message.reply_photo(hand, caption="Written by 🖊 [Anjal](t.me/anjalRobot)")


__mod_name__ = "🖊Write"

__help__ = """
 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
 """