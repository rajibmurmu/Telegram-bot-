import os
from pyrogram import Client, filters
from terabox_extract import get_terabox_direct_link

# ✅ টোকেন নেওয়া হচ্ছে পরিবেশ থেকে
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ✅ বট ক্লায়েন্ট তৈরি
app = Client("terabox_bot", bot_token=BOT_TOKEN)

# ✅ /start কমান্ড হ্যান্ডলার
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 স্বাগতম! একটা TeraBox লিংক দিন, ভিডিও পাঠিয়ে দিচ্ছি...")

# ✅ টেক্সট হ্যান্ডলার (যদি কেউ TeraBox লিংক দেয়)
@app.on_message(filters.text & filters.private)
async def handle_link(client, message):
    url = message.text.strip()

    if "terabox.com" not in url:
        return await message.reply_text("❌ এটা একটি TeraBox লিংক নয়!")

    await message.reply_text("🔍 লিংক যাচাই করছি, অপেক্ষা করুন...")

    try:
        direct = get_terabox_direct_link(url)
        if not direct:
            return await message.reply_text("❌ ভিডিও লিংক পাওয়া যায়নি!")

        await message.reply_text("📤 ভিডিও পাঠানো হচ্ছে...")
        await client.send_video(chat_id=message.chat.id, video=direct)

    except Exception as e:
        await message.reply_text(f"❌ একটি ত্রুটি ঘটেছে: {e}")

# ✅ বট চালানোর অংশ (main block)
if __name__ == "__main__":
    print("🤖 Bot is starting...")
    try:
        app.run()
    except Exception as e:
        print(f"❌ Error during bot start: {e}")
