from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from HeartBeat import app 
from config import SUPPORT_CHAT

#SUPPORT_CHAT = "aj_bioo"

@app.on_message(filters.command("wish"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("ᴀᴅᴅ ᴡɪꜱʜ ʙᴀʙʏ🦋!")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"✨ ʜᴇʏ! {m.from_user.first_name}! "
    wish += f"✨ ʏᴏᴜʀ ᴡɪꜱʜ: {text} "
    wish += f"✨ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ: {wish_count}%"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@app.on_message(filters.command("cute"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🎉 {mention} {mm}% ᴄᴜᴛᴇ ʙᴀʙʏ🦋"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

#----------HUG & KISS------------

# Hug GIFs
HUGGY = [
    "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif",
    "https://64.media.tumblr.com/d701f53eb5681e87a957a5ywu7980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif",
    "https://media.tenor.com/3Z9xwJ7XxJgAAAAC/anime-hug.gif",
    "https://media.tenor.com/Xb9L0Wb2X5oAAAAC/hug-anime.gif",
]

# Kiss GIFs
KISSY = [
    "https://media.tenor.com/9bK6gJ7M8o8AAAAC/anime-kiss.gif",
    "https://media.tenor.com/YdU3jKJQXfAAAAAC/kiss-anime.gif",
    "https://media.tenor.com/VcS-5mJ4JtoAAAAC/kiss.gif",
    "https://media.tenor.com/lBqC7V2zS6AAAAAC/couple-anime.gif",
]


# Hug Command
@app.on_message(filters.command("hug"))
async def hug(_, m):
    if len(m.command) < 2:
        await m.reply("ᴀᴅᴅ ʜᴜɢ ᴍᴇꜱꜱᴀɢᴇ 🫂✨!")
        return 

    url = random.choice(HUGGY)  # random hug gif
    text = m.text.split(None, 1)[1]
    hug_count = random.randint(1, 100)

    hug_msg = f"🤗 ʙᴀʙʏ {m.from_user.first_name}\n"
    hug_msg += f"🫂 ᴡᴀɴᴛ ᴛᴏ ᴋɪꜱꜱ {text}\n"
    hug_msg += f"✨ᴍᴏʀᴇ... ❤️ʟɪᴋᴇ ᴛʜɪꜱ...\n ᴘᴏᴡᴇʀ ʟᴇᴠᴇʟ: {hug_count}% \n\n ᴄᴀɴ ᴡᴇ ᴛʀʏ... 🙈ʜᴏɴᴇʏ"

    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=hug_msg,
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


# Kiss Command
@app.on_message(filters.command("kiss"))
async def kiss(_, m):
    if len(m.command) < 2:
        await m.reply("ᴀᴅᴅ ᴋɪss ᴍᴇꜱꜱᴀɢᴇ 😘✨!")
        return 

    url = random.choice(KISSY)  # random kiss gif
    text = m.text.split(None, 1)[1]
    kiss_count = random.randint(1, 100)

    kiss_msg = f"😘 ʙᴀʙʏ {m.from_user.first_name}\n"
    kiss_msg += f"💋 ᴡᴀɴᴛ ᴛᴏ ᴋɪꜱꜱ {text}\n"
    kiss_msg += f"✨ ᴍᴏʀᴇ... ❤️ʟɪᴋᴇ ᴛʜɪꜱ...\n ꜱᴡᴇᴇᴛɴᴇꜱꜱ ʟᴇᴠᴇʟ: {kiss_count}% \n\n ᴄᴀɴ ᴡᴇ ᴛʀʏ... 🙈ʜᴏɴᴇʏ"

    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=kiss_msg,
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


#--------------HUG & KISS -------

    
help_text = """
» ᴡʜᴀᴛ ɪꜱ ᴛʜɪꜱ (ᴡɪꜱʜ):
ʏᴏᴜ ʜᴀᴠɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ 
(ᴡɪꜱʜᴇꜱ) ʏᴏᴜ ᴄᴀɴ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʜᴏᴡ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ʏᴏᴜʀ ᴡɪꜱʜ!
ᴇxᴀᴍᴘʟᴇ:» /wish : ɪ ᴡᴀɴᴛ ᴄʟᴀꜱꜱ ᴛᴏᴘᴘᴇʀ 
» /wish : ɪ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ɪᴘʜᴏɴᴇ 
» /cute : ʜᴏᴡ ᴍᴜᴄʜ ɪ ᴀᴍ ᴄᴜᴛᴇ 
» /kiss : ʜᴏᴡ sᴘᴇᴄɪᴀʟ ɪs ᴀ ᴋɪss
» /hug  : ʜᴏᴡ ᴛɪɢʜᴛ ᴍʏ ʜᴜɢ
"""
