from pyrogram import Client, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
VERCEL_URL = os.getenv("VERCEL_URL")

app = Client(
    "file-store-bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Bot is running!\nSend me a file to generate a link.")

# File handler
@app.on_message(filters.video | filters.document | filters.photo)
async def file_handler(client, message):

    if message.video:
        file_id = message.video.file_id

    elif message.document:
        file_id = message.document.file_id

    elif message.photo:
        file_id = message.photo[-1].file_id

    else:
        return

    link = f"{VERCEL_URL}/access/{file_id}"

    await message.reply_text(f"🔗 Your File Link:\n{link}")

app.run()
