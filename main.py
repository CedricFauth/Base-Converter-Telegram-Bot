from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


if __name__ == "__main__":
    TOKEN = os.getenv('BOT_TOKEN')
    if TOKEN:
        updater = Updater(TOKEN)

        updater.dispatcher.add_handler(CommandHandler('hello', hello))

        updater.start_polling()
        updater.idle()
    else:
        print("Token not set run: source .env")
