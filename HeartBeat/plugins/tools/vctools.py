import asyncio
from typing import Optional, List, Union
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPrivileges, VideoChatEnded
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import ChatAdminRequired

from HeartBeat import app, Userbot
from HeartBeat.utils.database import *
from HeartBeat.core.call import GhosttBatt  # This is the Call class instance from File 1
from HeartBeat.utils.admin_filters import admin_filter
from config import BANNED_USERS

from pytgcalls.types import MediaStream, AudioQuality
from pytgcalls.exceptions import NoActiveGroupCall


# -------------------- VC INFO --------------------
@app.on_message(filters.command(["vcinfo"], ["/", "!"]))
async def strcall(client, message: Message):
    assistant = await group_assistant(GhosttBatt, message.chat.id)
    try:
        # Join call with local audio file using new API
        stream = MediaStream(
            "./HeartBeat/assets/call.mp3",
            audio_parameters=AudioQuality.HIGH,
            video_flags=MediaStream.IGNORE
        )

        await assistant.join_group_call(message.chat.id, stream)

        text = "- Beloveds in the call 🫶 :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            mut = "ꜱᴘᴇᴀᴋɪɴɢ 🗣" if not participant.muted else "ᴍᴜᴛᴇᴅ 🔕"
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ➤ {user.mention} ➤ {mut}\n"

        text += f"\nɴᴜᴍʙᴇʀ ᴏꜰ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛꜱ : {len(participants)}"
        await message.reply(text)

        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)

    except NoActiveGroupCall:
        await message.reply("ᴛʜᴇ ᴄᴀʟʟ ɪꜱ ɴᴏᴛ ᴏᴘᴇɴ ᴀᴛ ᴀʟʟ")
    except Exception as e:
        if "already joined" in str(e).lower():
            text = "ʙᴇʟᴏᴠᴇᴅꜱ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 🫶 :\n\n"
            participants = await assistant.get_participants(message.chat.id)
            k = 0
            for participant in participants:
                mut = "ꜱᴘᴇᴀᴋɪɴɢ 🗣" if not participant.muted else "ᴍᴜᴛᴇᴅ 🔕"
                user = await client.get_users(participant.user_id)
                k += 1
                text += f"{k} ➤ {user.mention} ➤ {mut}\n"
            text += f"\nɴᴜᴍʙᴇʀ ᴏꜰ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛꜱ : {len(participants)}"
            await message.reply(text)
        else:
            await message.reply(f"Unexpected error: <code>{str(e)}</code>")


# -------------------- GROUP CALL HELPERS --------------------
async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await assistant.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"No group ᴠᴏɪᴄᴇ ᴄʜᴀᴛ Found** {err_msg}")
    return False


# -------------------- START VC --------------------
@app.on_message(filters.command(["vcstart", "startvc"], ["/", "!"]))
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "ᴇʀʀᴏʀ ᴡɪᴛʜ ᴀꜱꜱɪꜱᴛᴀɴᴛ")
        return
    msg = await app.send_message(chat_id, "ꜱᴛᴀʀᴛɪɴɢ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ⚡️~!")
    except ChatAdminRequired:
        try:
            await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_video_chats=True
            ))
            peer = await assistant.resolve_peer(chat_id)
            await assistant.invoke(
                CreateGroupCall(
                    peer=InputPeerChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash,
                    ),
                    random_id=assistant.rnd_id() // 9000000000,
                )
            )
            await msg.edit_text("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ⚡️~!")
        except:
            await msg.edit_text("ɢɪᴠᴇ ᴛʜᴇ ʙᴏᴛ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ⚡")


# -------------------- END VC --------------------
@app.on_message(filters.command(["vcend", "endvc"], ["/", "!"]))
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "ᴇʀʀᴏʀ ᴡɪᴛʜ ᴀꜱꜱɪꜱᴛᴀɴᴛ")
        return
    msg = await app.send_message(chat_id, "ᴄʟᴏꜱɪɴɢ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..")
    try:
        if not (
            group_call := (
                await get_group_call(assistant, m, err_msg=", ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
            )
        ):
            return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴄʟᴏꜱᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ⚡️~!")
    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            try:
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                    can_manage_video_chats=True
                ))
                if not (
                    group_call := (
                        await get_group_call(assistant, m, err_msg=", ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
                    )
                ):
                    return
                await assistant.invoke(DiscardGroupCall(call=group_call))
                await msg.edit_text("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴄʟᴏꜱᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ⚡️~!")
            except:
                await msg.edit_text("ɢɪᴠᴇ ᴛʜᴇ ʙᴏᴛ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ")


# -------------------- VOLUME CONTROL --------------------
@app.on_message(filters.command("volume") & filters.group & admin_filter & ~BANNED_USERS)
async def set_volume(client, message: Message):
    chat_id = message.chat.id

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ Usage: <code>/volume 1-200</code>")

    try:
        volume_level = int(args[1])
    except ValueError:
        return await message.reply_text("❌ Invalid number. Please use <code>/volume 1-200</code>")

    if volume_level == 0:
        return await message.reply_text("🔇 Use <code>/mute</code> to mute the stream.")

    if not 1 <= volume_level <= 200:
        return await message.reply_text("⚠️ Volume must be between 1 and 200.")

    if chat_id >= 0:
        return await message.reply_text("❌ Volume control is not supported in basic groups.")

    try:
        await GhosttBatt.change_volume(chat_id, volume_level)
        await message.reply_text(
            f"<b>🔊 Stream volume set to {volume_level}</b>.\n\n└ Requested by: {message.from_user.mention} 🦋"
        )
    except Exception as e:
        await message.reply_text(f"❌ Failed to change volume.\n<b>Error:</b> {e}")
