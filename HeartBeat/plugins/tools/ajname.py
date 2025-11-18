import re
from pyrogram import filters
import random
from HeartBeat import app


@app.on_message(filters.command(["J", "j", "lovely", "Lovely], prefixes=["Aj", "a", "A"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAEBy01pHE10GuzPrP7LcKFj-JwZqeBAEQAC3BgAAo_oWFTHiufz8tnEQh4E",
        "CAACAgUAAxkBAAEBy01pHE10GuzPrP7LcKFj-JwZqeBAEQAC3BgAAo_oWFTHiufz8tnEQh4E",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "✨",
        "✨",
        "✨",
    ]
    return random.choice(emojis)
