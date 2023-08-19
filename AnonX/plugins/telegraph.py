from telegraph import upload_file
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import app

@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = message.reply("ᴜᴘʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        button = InlineKeyboardButton(text="ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ", url=url)
        markup = InlineKeyboardMarkup([[button]])

        if reply.photo:
            message.reply_photo(photo=reply.photo.file_id, reply_markup=markup)
        else:
            message.reply_text("ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ:", reply_markup=markup)
        
        i.delete()
    elif reply and not reply.media:
        message.reply_text("ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
    else:
        message.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴍᴇssᴀɢᴇ...")
