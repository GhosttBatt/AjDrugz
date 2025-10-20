import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from HeartBeat.utils.errors import capture_err 
from HeartBeat import app
from config import BOT_USERNAME

# Caption Text
start_txt = """<b>✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <u>ʜᴇᴀʀᴛʙᴇᴀᴛ ʀᴇᴘᴏs</u></b>

🚀 <b>ᴇᴀsʏ ᴅᴇᴘʟᴏʏ</b> –ᴏɴᴇ ᴄʟɪᴄᴋ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ  
🛡️ <b>ɴᴏ ʜᴇʀᴏᴋᴜ ᴏʀ ɪᴅ ʙᴀɴ ɪssᴜᴇs</b>  
🔋 <b>ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs</b> – ʀᴜɴ 24/7 ʟᴀɢɢ-ғʀᴇᴇ  
⚙️ <b>ғᴜʟʟʏ ғᴜɴᴄᴛɪᴏɴᴀʟ & ᴇʀʀᴏʀ-ғʀᴇᴇ</b>  

<i>ɴᴇᴇᴅ ʜᴇʟᴘ? sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴛᴏ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ!</i>"""

# Repo Command Handler
@app.on_message(filters.command("repo"))
async def repo_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/HeartBeat_Fam"),
            InlineKeyboardButton("👤 ᴏᴡɴᴇʀ", url="https://t.me/rajeshrakis"),
        ],
        [InlineKeyboardButton("🧾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/HeartBeat_Offi")],
        [
            InlineKeyboardButton("ꜱɪʟᴜᴋᴋᴜ ᴍᴜꜱɪᴄ", url="https://t.me/SilukkuMusicBot"),
            InlineKeyboardButton("ꜱɪʟᴜᴋᴋᴜ ᴄʜᴀᴛ", url="https://t.me/SilukkuChatBot"),
        ],
        [
            InlineKeyboardButton("ᴄʟᴏɴᴇ ᴍᴜꜱɪᴄ", url="https://t.me/CloneMusicRobot"),
            InlineKeyboardButton("ʜʙ-ᴍᴜꜱɪᴄ", url="https://t.me/Thedakkidaikathaval_Bot"),
        ],
        [
            InlineKeyboardButton("ᴍᴏᴠɪᴇꜱ", url="https://t.me/HeartBeatMovies_Bot"),
            InlineKeyboardButton("ᴡᴇʙ-ꜱᴇʀɪᴇꜱ", url="https://t.me/HeartBeatTV_Bot"),
        ],
        [
            InlineKeyboardButton("ꜱᴛʀɪɴɢ-ɢᴇɴ", url="https://t.me/Heart2Beat_Bot"),
            InlineKeyboardButton("ᴜꜱᴇʀʙᴏᴛ", url="https://t.me/CloneUserBot"),
        ],
    ]

    await msg.reply_photo(
        photo="https://files.catbox.moe/lr39gb.jpg",
        caption=start_txt,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/rajeshrakis")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/HeartBeat_Fam) | [UPDATES](https://t.me/HeartBeat_Offi)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="HB contributors.")


