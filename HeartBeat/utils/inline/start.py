from pyrogram.types import InlineKeyboardButton

import config
from HeartBeat import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [   
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
            #InlineKeyboardButton(text= "⌯ ᴧʟʟ ʙᴏᴛ𝗌 ⌯", url=f"https://t.me/HeartBeat_Offi/13")
        ]
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_USERNAME),
            #InlineKeyboardButton(text="⌯ ᴧʟʟ ʙᴏᴛ𝗌 ⌯" ,url=f"https://t.me/HeartBeat_Offi/13")
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
