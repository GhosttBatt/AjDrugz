import asyncio
import importlib

from pyrogram import idle
import config
from HeartBeat import LOGGER, app, userbot
from HeartBeat.core.call import GhosttBatt
from HeartBeat.misc import sudo
from HeartBeat.plugins import ALL_MODULES
from HeartBeat.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if not any([
        config.STRING1,
        config.STRING2,
        config.STRING3,
        config.STRING4,
        config.STRING5,
    ]):
        LOGGER(__name__).error(
            "String session(s) not provided; please fill Pyrogram session"
        )
        exit()

    await sudo()
    try:
        for user in await get_gbanned():
            BANNED_USERS.add(user)
        for user in await get_banned_users():
            BANNED_USERS.add(user)
    except Exception:
        pass

    await app.start()
    for mod in ALL_MODULES:
        importlib.import_module("HeartBeat.plugins." + all_module)
    LOGGER("HeartBeat.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    await userbot.start()
    await GhosttBatt.start()

    try:
        await GhosttBatt.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except Exception as e:
        err = str(e).lower()
        if "start" in err or "create call first" in err or "group call not found" in err:
            LOGGER("HeartBeat").error(
                "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗔𝗧 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
            )
            exit()
        # Ignore all other exceptions silently
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
