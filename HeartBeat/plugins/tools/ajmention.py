import re
from pyrogram import filters
import random
from VIPMUSIC import app


###### GOOOD MORNING 
@app.on_message(filters.command(["m","oodmorning","orning"], prefixes=["g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_video = random.choice([True, False])
    if send_video:
        video_id = get_random_video()
        app.send_video(message.chat.id, video_id)
        message.reply_text(f"**Good Morning, {sender}! Wakeup fast. 🥰**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Good Morning, {sender}! Wakeup fast. {emoji}**")


def get_random_video():
    videos = [
        "https://files.catbox.moe/a8e9kk.mp4",
        "https://files.catbox.moe/a8e9kk.mp4"
    ]
    return random.choice(videos)


def get_random_emoji():
    emojis = [
        "✨",
        "✨",
        "✨",
    ]
    return random.choice(emojis)
