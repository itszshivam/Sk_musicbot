from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐏ᴇʀsᴏɴᴀ𝐋",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="𝐆ʟᴏʙᴀ𝐋", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂ʟᴏs𝐄 ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐓ᴏ𝐏 10 𝐏ʟᴀʏʟɪsᴛ𝐒", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐏ᴇʀsᴏɴᴀ𝐋", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐆ʟᴏʙᴀ𝐋", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝐆ʀᴏᴜ𝐏'𝐒", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄ𝐊", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏs𝐄", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴜᴅɪ𝐎", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝐕ɪᴅᴇ𝐎", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁ᴀᴄ𝐊", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="𝐂ʟᴏs𝐄", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴅᴇʟᴇᴛᴇ",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐁ᴀᴄ𝐊",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="𝐂ʟᴏs𝐄",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ ᴄʟᴏsᴇ ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
