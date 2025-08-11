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
from pytgcalls.exceptions import CallBeforeStartError, PytgcallsError, GroupCallNotFoundError
from ntgcalls import TelegramServerError  # Keep if used elsewhere

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
        importlib.import_module("HeartBeat.plugins" + mod)
    LOGGER("HeartBeat.plugins").info("Loaded all features!")

    await userbot.start()
    await GhosttBatt.start()

    try:
        await GhosttBatt.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except (CallBeforeStartError, GroupCallNotFoundError):
        LOGGER("HeartBeat").error(
            "Please start your group voice chat/channel first. HeartBeat bot stopped."
        )
        exit()
    except Exception:
        pass

    await GhosttBatt.decorators()
    LOGGER("HeartBeat").info(
        "╔═════ Made by HEARTBEAT ═════╗"
    )

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("HeartBeat").info("Stopped HeartBeat Music Bot.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
