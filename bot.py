from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, VERCEL_URL

app = Client(
    "filestorebot",
    bot_token=8240874907:AAEvesmr0JbkAAynmLLQtQBR8EOVzqMXTEM,
    api_id=21592881,
    api_hash=eba06a0d465f1d1797f0e92e97ac68ad
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Hello!\n\nSend me any file and I will generate a secure download link."
    )

@app.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def store_file(client, message):

    if message.document:
        file_id = message.document.file_id
    elif message.video:
        file_id = message.video.file_id
    elif message.audio:
        file_id = message.audio.file_id
    else:
        return

    link = f"{VERCEL_URL}/access/{file_id}"

    await message.reply_text(
        f"✅ File Stored Successfully!\n\n"
        f"🔗 Your Secure Link:\n{link}"
    )

app.run()
