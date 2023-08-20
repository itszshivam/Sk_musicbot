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
        photo=f"https://telegra.ph/file/7f2de6a3d5990a88bab86.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☆𝗦𝐇𝗜𝐕𝗔𝐌☆", url=f"https://t.me/itsz_shivam")
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
        photo=f"https://telegra.ph/file/7f2de6a3d5990a88bab86.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☆𝗦𝐇𝗜𝐕𝗔𝐌☆", url=f"https://t.me/itsz_shivam")
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
        photo=f"https://telegra.ph/file/7f2de6a3d5990a88bab86.jpg",
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
        photo=f"https://telegra.ph/file/7f2de6a3d5990a88bab86.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://telegra.ph/file/a1feb673365b2b271efb6.jpg")
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
        photo=f"https://telegra.ph/file/7f2de6a3d5990a88bab86.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://github.com/itszshivam/sk_musicbot")
                ]
            ]
        ),
    
