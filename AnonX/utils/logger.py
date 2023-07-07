from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**{MUSIC_BOT_NAME} 𝐏𝐋𝐀𝐘 𝐋𝐎𝐆𝐆𝐄𝐑**

**𝐂𝐇𝐀𝐓:** {message.chat.title} [`{message.chat.id}`]
**𝐔𝐒𝐄𝐑:** {message.from_user.mention}
**𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄:** @{message.from_user.username}
**𝐈𝐃:** `{message.from_user.id}`
**𝐂𝐇𝐀𝐓 𝐋𝐈𝐍𝐊:** {chatusername}

**sᴇᴀʀᴄʜᴇᴅ ғᴏʀ:** {message.text}

**sᴛʀᴇᴀᴍ ᴛʏᴩᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
