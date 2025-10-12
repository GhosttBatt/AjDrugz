import asyncio
import importlib
import threading
import requests
from flask import Flask

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from HeartBeat import LOGGER, app, userbot
from HeartBeat.core.call import GhosttBatt
from HeartBeat.misc import sudo
from HeartBeat.plugins import ALL_MODULES
from HeartBeat.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# ─────────────────────────────────────────────
# KEEP-ALIVE SECTION (Flask + Auto-Ping)
# ─────────────────────────────────────────────

PING_URL = "https://ajdrugz.onrender.com"  # ✅ Your Render URL

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is alive!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=8080)

def start_flask():
    thread = threading.Thread(target=run_flask)
    thread.daemon = True
    thread.start()

async def auto_ping():
    while True:
        try:
            requests.get(PING_URL)
        except Exception as e:
            print("Ping failed:", e)
        await asyncio.sleep(300)  # 300 seconds

# ─────────────────────────────────────────────

async def init():
    start_flask()                 # ✅ Start Flask Web Server
    asyncio.create_task(auto_ping())  # ✅ Start Auto-Pinger

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("HeartBeat.plugins" + all_module)
    LOGGER("HeartBeat.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await GhosttBatt.start()
    try:
        await GhosttBatt.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("HeartBeat").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗔𝗧 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await GhosttBatt.decorators()
    LOGGER("HeartBeat").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗔𝗧\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("HeartBeat").info("𝗦𝗧𝗢𝗣 𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗔𝗧 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
