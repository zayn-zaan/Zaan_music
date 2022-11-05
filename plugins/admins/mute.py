# Powered By @AdityaHalder

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules import app
from modules.core.call import Aditya
from modules.utils.helpers.filters import command
from modules.utils.database import is_muted, mute_on
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    command(["mute", "cmute"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if await is_muted(chat_id):
        return await message.reply_text("**🔇 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐌𝐮𝐭𝐞𝐝 🌷 ...**")
    await mute_on(chat_id)
    await Aditya.mute_stream(chat_id)
    await message.reply_text("**🔇 𝐌𝐮𝐭𝐞𝐝 🌷 ...**")
