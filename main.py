import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")
LINK = os.getenv("SHEIN_LINK")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 أهلاً بك!\n\n" + str(LINK))

def main():
    if not TOKEN:
        print("Missing BOT_TOKEN")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
