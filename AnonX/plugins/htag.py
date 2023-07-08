from AnonX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

TAGMES = [ " **चलो एक पार्टी करते हैं 🥳🥳** ",
                     " **आप ग्रुप में बात क्यों नहीं करते 😒😒** ",
                     " **खुश रहो✌️🙂** ",
                     " **माँ ने मुझे डाँटा 🥲** ",
                     " **आप कल कहाँ गए थे? 🤔** ",
                     " **क्या चल रहा है इन दिनों 😌❤️🥀** ",
                     " **नमस्ते 👀** ",
                     " **हम मित्र हो सकते हैं ?** ",
                     " **आप कॉलेज या स्कूल में हैं** ",
                     " **गलत मत कहो 🙊** ",
                     " **मुझे देखो 😒❤️👀** ",
                     " **आज क्यों खफा हो...? 😒** ",
                     " **नमस्ते 😈** ",
                     " **मुझे अपने ग्रुप में शामिल करें मैं सभी को टैग कर दूंगी ❤️** ",
                     " **क्या आप मेरे दोस्त हैं 😒😒** ",
                    " **कल मज़ा आया 🥳🥳** ",
                    " **आपने भोजन कर लिया 😚** ",
                    " **बहुत तेज़ जा रहे हो 😏😏** ",
                    " **मैं कल खरीदारी के लिए जाना चाहती हूँ 💞** ",
                    " **क्या आप रिश्ते में हैं? 👀** ",
                    " **और कैदी कैसा है 👀** ",
                    " **क्या आप मुझे कभी याद करते हो 🥺🥺** ",
                    " **मुझे भूल गए 🥺🥀** ",
                    " **आज मैंने बंदर देखा 😌👉🐒** ",
                    " **बात करो यार ❤️👀** ",
                    " **वॉयस चैट पर आइए** ",
                    " **वॉयस चैट पर लडाई हो रही 🤯🤯** ",
                    " **मुझे कभी याद नहीं करते 💔💔** ",
                    " **हाँ 👀** ",
                    " **दोस्त आप कहां हैं ❤️💫** ",
                    " **मुझे अपने ग्रुप में जोड़ें 🥺** ",
                    " **यहाँ आओ @INCRICIBLE 👀** ",
                    " **आप सो गए क्या 🤔🤔** ",
                    " **नमस्ते जी 💞** ",
                    " **अगर आपके जैसा दोस्त है तो इसमें चिंता की क्या बात है?❣️** ",
                    " **कितने खामोश हो यार 😒** ",
                    " **आप गाना जानते हैं 👀** ",
                    " **शांत हो जाओ हर कोई** ",
                    " **हाय 👀** ",
                    " **आप के घर में सब कैसे हैं 😌❤️🥀** ",
                    " **उठो भी 😶** ",
                    " **आप कब से हैं 🧐** ",
                    " **मैंने #𝗔𝗽𝗻𝗲 ख्वाहिशो😇 को दिवार 𝗠𝗮𝗶𝗻 चुनवा दिया, खामखाँ #𝗭𝗶𝗻𝗱𝗲𝗴𝗶 में अनारकली💃बनके नाच रही थी** ",
                    " **नींदे उडा रख्खी है #𝗠𝗘𝗥𝗜 किसी ने.... ये कहकर की... 𝗧𝗨𝗠👉 मुझे अच्छे लगते 𝗛𝗢..😘😘** ",
                    " **𝗦𝗨𝗡𝗢👂👂👂… तुम👧 ही रख लो अपना बना कर औरों ने तो छोड़ दिया #_𝗧𝗨𝗠𝗛𝗔𝗥𝗔👉 समझकर..!!😔** ",
                    " **नींदे उडा रख्खी है #𝗠𝗘𝗥𝗜 किसी ने.... ये कहकर की... 𝗧𝗨𝗠👉 मुझे अच्छे लगते 𝗛𝗢..😘😘 ** ",
                    " **#_𝗗𝗜𝗟💖 तो हर किसी के पास होता हैँ, लेकिन सब #𝗗𝗜𝗪𝗔𝗟𝗘💑 नहीँ❌ होते…** ",
                    ]



@app.on_message(filters.command(["htag"," hstag", "hftag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Only admin can use this command!")

    if message.reply_to_message and message.text:
        return await message.reply("/htag Try this next time for tagging..")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/htag hii 👈 Try this or reply any message...")
    else:
        return await message.reply("/htag hii 👈 Try this or reply any message...")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("No active mention process is started by me.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("This command is only for admins. You can't use this command.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ Mention process stopped ♦")
