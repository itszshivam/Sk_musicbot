import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app  

photo = [
    "https://graph.org/file/49c7711765c285f7e653a.mp4",
    "https://graph.org/file/0bb559bf659fbae560246.mp4",
    "https://graph.org/file/edabd6a56cd7e13d7b6bb.mp4",
    "https://graph.org/file/11e823c75b26c70c76d22.mp4",
    "https://graph.org/file/892490a7d76a662a1728f.mp4",
    "https://graph.org/file/cb39dcc6a20fdf631161f.mp4",
    "https://graph.org/file/4dae8308f03b43d289b95.mp4",
    "https://graph.org/file/39662f7a343e2a95ea5c4.mp4",
    "https://graph.org/file/8155d0dccaca1dd7e9994.jpg",
    "https://graph.org/file/7d8afb4982c1949f0c9da.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**𝐇ᴇʏ {message.from_user.mention}🌹**\n\n◈ •━━━━━ ⸙ ♡ ⸙ ━━━━━• ◈\n"
                f"**𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ** {message.chat.title}💥\n"
                f"**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{message.chat.username}💫\n"
                f"**𝐘ᴏᴜʀ 𝐈𝐃:** {message.from_user.id}💌\n"
                f"**𝐘ᴏᴜʀ 𝐔sᴇʀɴᴀᴍᴇ:** @{message.from_user.username}👀\n"
                f"**𝐘ᴏᴜ 𝐀ʀᴇ {count} 𝐌ᴇᴍʙᴇʀ𝐬 𝐇ᴇʀᴇ🤩**\n◈ •━━━━━ ⸙ ♡ ⸙ ━━━━━• ◈\n\n"
                f"**𝐈 𝐇ᴏᴘᴇ 𝐘ᴏᴜ 𝐀ʀᴇ 𝐄ɴᴊᴏʏɪɴɢ 𝐘ᴏᴜʀ 𝐃ᴀʏ!!💝\n"
                f"**𝐊ᴇᴇᴘ 𝐒ᴍɪʟɪɴɢ! 𝐆ᴏᴅ 𝐁ʟᴇss 𝐘ᴏᴜ!!😄"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"👽𝐓ᴇʟᴇᴘᴏʀᴛ 𝐌ᴇ 𝐅ʀᴏᴍ 𝐇ᴇʀᴇ👽", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
