import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from HeartBeat.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False

START_IMG_URLS = "https://graph.org/file/ffdb1be822436121cf5fd.png"

MESSAGES = f"""<blockquote>✰ ᴍᴜsɪᴄ ✰ᴍᴇɴᴛɪᴏɴ ✰ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</blockquote>

𝘽𝙊𝙏 𝙁𝙀𝘼𝙏𝙐𝙍𝙀𝙎: (•‌ᴗ•‌)و
𝙄𝙢 𝙪𝙣𝙡𝙤𝙘𝙠𝙚𝙙 𝙢𝙮 𝙎𝙩𝙪𝙣𝙣𝙞𝙣𝙜 𝙋𝙧𝙤 𝙁𝙪𝙩𝙪𝙧𝙚𝙨 𝙞𝙣𝙨𝙞𝙙𝙚 𝙢𝙚:
<blockquote>⍟𝗌ᴜᴘᴘᴏʀᴛ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ𝗌 ⍟ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪᴄᴇ ⍟ ᴠᴄ-ɪɴᴠɪᴛᴇ ᴄᴀʀᴅ ⍟ ᴘʟᴀʏ ᴡɪᴛʜᴏᴜᴛ 𝗌ʟᴀ𝗌ʜ</blockquote>
😻ᴘʀᴏ ғᴇᴀᴛᴜʀᴇ𝗌 ᴜɴʟᴏᴄᴋᴇᴅ🥳
💕Sᴜᴘᴘᴏʀᴛ Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ Fᴇᴀᴛᴜʀᴇ𝗌🦋
𝑁𝑒𝑡𝑤𝑜𝑟𝑘 - [𝞖𝘌𝘈𝘙𝘛𝂬𓏲ࣹ᷼𝄢𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Offi) 😎✨"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖֯֟፝͢͡𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞֟֠֯፝͢͡𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ", url=f"https://t.me/HeartBeat_Fam")
        ]
    ]
)


caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=caption, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
