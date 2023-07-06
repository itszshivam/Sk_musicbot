from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ🌹",
                url=f"https://t.me/your_godfather_xd",
            )
        ],
    
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•🌷ᴏᴡɴᴇʀ🌷•",
                url=f"https://t.me/your_godfather_xd",
            )
        ],           
     ]
    return buttons
