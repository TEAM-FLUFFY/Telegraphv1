from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
π·π΄π {} π±ππΎ πΈπ°πΌ ππΈπΌπΏπ»π΄ ππ΄π»π΄πΆππ°πΏπ· π±πΎπ πΌπ°π³π΄ π±π @pushpa_Reju
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/2ad808f3e0ed97575a5c1.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("π£πΎπ βοΈ", url="t.me/pushpa_Reju"),
            InlineKeyboardButton("π§πππ³ππ΄ππΎ", callback_data="use") 
            ]]
            )
        )



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "use":
        await msg.answer("""Itβs simple to use me. Just send any photo or video below 5 MB and you will get the telegraph link
""", show_alert=True)

