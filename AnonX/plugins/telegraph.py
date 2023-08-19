from telegraph import upload_file
from pyrogram import filters
from AnonX import app


@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("🌹𝐌𝐚𝐤𝐢𝐧𝐠 𝐚 𝐥𝐢𝐧𝐤 𝐨𝐟 𝐲𝐨𝐮𝐫 𝐝𝐨𝐜𝐮𝐦𝐞𝐧𝐭... 𝐁𝐘 𝐏𝐇𝐀𝐍𝐓𝐎𝐌 𝐌𝐔𝐒𝐈𝐂🌹")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤  👉 {url})
