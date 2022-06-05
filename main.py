
import botapi as key
from telegram.ext import *
import respo as r

print("Bot Startet...")


def sc(update, context):
    update.message.reply_text('Type anything')


def hc(update, context):
    update.message.reply_text('If you need help ? You Should ask it to Google')


def h(update, context):
    text=str(update.message.text).lower()
    response = r.srepo(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():

    updater = Updater(key.API_Key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", sc))
    dp.add_handler(CommandHandler("help", hc))

    dp.add_handler(MessageHandler(Filters.text, h))

    dp.add_error_handler(error)

    updater.start_polling(0)
    updater.idle()
  


main()
