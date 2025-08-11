import asyncio
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from ntgcalls import TelegramServerError

from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality, Update

import config
from HeartBeat import LOGGER, app
from HeartBeat.misc import db
from HeartBeat.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
)
from HeartBeat.utils.exceptions import AssistantErr
from strings import get_string

autoend = {}
counter = {}
loop = asyncio.get_event_loop()


async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)


class Call(PyTgCalls):
    def __init__(self):
        self.userbots = [
            Client(
                name=f"HeartBeat{i}",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(getattr(config, f"STRING{i}")),
            )
            for i in range(1, 6)
        ]
        self.assistants = [PyTgCalls(ub, cache_duration=100) for ub in self.userbots]

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await _clear_(chat_id)
            await assistant.leave_group_call(chat_id)
        except Exception:
            pass

    async def join_call(
        self,
        chat_id: int,
        original_chat_id: int,
        link,
        video: Union[bool, str] = None,
        image: Union[bool, str] = None,
    ):
        assistant = await group_assistant(self, chat_id)
        language = await get_lang(chat_id)
        _ = get_string(language)

        stream = (
            MediaStream(
                link,
                audio_parameters=AudioQuality.HIGH,
                video_parameters=VideoQuality.SD_480p,
            )
            if video
            else MediaStream(
                link,
                audio_parameters=AudioQuality.HIGH,
                video_flags=MediaStream.IGNORE,
            )
        )

        try:
            await assistant.join_group_call(chat_id, stream)
        except Exception as e:
            err = str(e).lower()
            if "group call not found" in err or "create call first" in err:
                raise AssistantErr(_["call_8"])
            if "already joined" in err or "already in call" in err:
                raise AssistantErr(_["call_9"])
            if "phone.creategroupcall" in err:
                raise AssistantErr(_["call_8"])
            raise AssistantErr(_["call_10"])

        await add_active_chat(chat_id)
        await music_on(chat_id)
        if video:
            await add_active_video_chat(chat_id)

        if await is_autoend():
            counter[chat_id] = {}
            users = len(await assistant.get_participants(chat_id))
            if users == 1:
                autoend[chat_id] = datetime.now() + timedelta(minutes=1)

    async def change_stream(self, client, chat_id):
        check = db.get(chat_id) or []
        if not check:
            await _clear_(chat_id)
            return await client.leave_group_call(chat_id)

        queued = check[0]["file"]
        language = await get_lang(chat_id)
        _ = get_string(language)
        video = str(check[0]["streamtype"]) == "video"

        stream = (
            MediaStream(
                queued,
                audio_parameters=AudioQuality.HIGH,
                video_parameters=VideoQuality.SD_480p,
            )
            if video
            else MediaStream(
                queued,
                audio_parameters=AudioQuality.HIGH,
                video_flags=MediaStream.IGNORE,
            )
        )

        try:
            await client.change_stream(chat_id, stream)
        except Exception:
            await app.send_message(check[0]["chat_id"], text=_["call_6"])
            return

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Clients...")
        for assistant in self.assistants:
            await assistant.start()

    def decorators(self):
        for assistant in self.assistants:
            @assistant.on_stream_end()
            async def handler(client, update: Update):
                # Simply handle the stream end without checking type
                await self.change_stream(client, update.chat_id)


GhosttBatt = Call()
