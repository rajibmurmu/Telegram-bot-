import os
from pyrogram import Client, filters
from terabox_extract import get_terabox_direct_link

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("terabox_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 স্বাগতম! একটা TeraBox লিংক দিন, ভিডিও পাঠিয়ে দিচ্ছি...")

@app.on_message(filters.text & filters.private)
async def handle_link(client, message):
    url = message.text.strip()
    if "terabox.com" not in url:
        return await message.reply_text("❌ দুঃখিত, এটা TeraBox লিংক না মনে হচ্ছে।")
    await message.reply_text("⏳ ভিডিও লিংক বের করছি, অপেক্ষা করুন...")
    direct = get_terabox_direct_link(url)
    if not direct:
        return await message.reply_text("❌ সরাসরি ডাউনলোড লিংক পাওয়া যায়নি।")
    await client.send_video(message.chat.id, direct)