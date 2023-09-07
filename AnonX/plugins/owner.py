from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/719356976c0a6f14f6ada.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☆˹𝐙ҽнα𝐑☆", url=f"https://t.me/zehar3_bot")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/719356976c0a6f14f6ada.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☆˹𝐙ҽнα𝐑☆", url=f"https://t.me/zehar3_bot")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b11804358865ade675957.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://github.com/itszshivam/sk_musicbot")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b11804358865ade675957.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://te.legra.ph/file/ebc3fc421b8776e29ad98.mp4")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b11804358865ade675957.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://github.com/itszshivam/sk_musicbot")
                ]
            ]
        ),
    )
