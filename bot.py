from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "8240874907:AAGjzRy9fkZy-cvw9rN4Wmb25Noil4_M6Fk"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Bot is running!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Send me a file and I will generate a link.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
