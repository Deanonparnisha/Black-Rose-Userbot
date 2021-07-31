
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("afk" , prefixes="..") & filters.me)
async def fac(client: Client, message: Message):
	await message.edit("<code>.afk</code>")
