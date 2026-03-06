from pyrogram import Client, filters
import os

BOT_TOKEN = os.getenv("8240874907:AAGjzRy9fkZy-cvw9rN4Wmb25Noil4_M6Fk")
API_ID = int(os.getenv("21592881"))
API_HASH = os.getenv("eba06a0d465f1d1797f0e92e97ac68ad")
VERCEL_URL = os.getenv("https://heaven-verse.vercel.app")

app = Client(
    "file-store-bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Bot is running!")

@app.on_message(filters.document | filters.video | filters.photo)
async def file_handler(client, message):
    file_id = message.document.file_id if message.document else message.video.file_id if message.video else message.photo.file_id
    
    link = f"{VERCEL_URL}/access/{file_id}"
    
    await message.reply_text(f"🔗 Your link:\n{link}")

app.run()
