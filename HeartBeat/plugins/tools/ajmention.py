import re
from pyrogram import filters
import random
from HeartBeat import app


###### GOOOD MORNING 
@app.on_message(filters.command(["xiaoyu_fan","li_xiaoyu_fan","@li_xiaoyu_fan"], prefixes=["@li_","@",""]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_video = random.choice([True, False])
    if send_video:
        video_id = get_random_video()
        app.send_video(message.chat.id, video_id)
        message.reply_text(f"**🦋му αттιтυ∂є ιѕ ∂єρєη∂ ση тнιѕ ρєяѕση {sender}...ωнσ ιѕ ѕтαη∂ιηg σƒ мє...𝆺꯭𝅥⎯꯭**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**കണ്ട് മുട്ടുന്ന ഓരോ മനുഷ്യരും {sender} സ്ഥിരമെന്ന് കരുതരുത്..🕊 {emoji}**")


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
