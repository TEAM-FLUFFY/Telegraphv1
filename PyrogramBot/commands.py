from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
𝙷𝙴𝚈 {} 𝙱𝚁𝙾 𝙸𝙰𝙼 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙿𝙷 𝙱𝙾𝚃 𝙼𝙰𝙳𝙴 𝙱𝚈 @pushpa_Reju
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/b5267f29b7c2eb523b516.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖣𝖾𝗏 ⚙️", url="t.me/pushpa_Reju")
