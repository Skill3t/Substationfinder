#!/bin/sh
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import time
import localdb
import configparser
import logging

logging.basicConfig(filename='Main.log', level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')


TOKEN_TELEGRAM = None
config = configparser.ConfigParser()
config.read('production.ini')
TOKEN_TELEGRAM = str(config['DEFAULT']['TelegrammKey'])

mybots = {}


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        """Hallo. Ich bin dein Umspannanlagen Bot.

Ich kann Dir zeigen wo sich Umspannanlagen in Deutschland befinden

Tippe den Namen oder Teile des Namens ein um Umspannanlagen zu finden.

"""
    )


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logging.error('Update "%s" caused error "%s"', update, error)


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Suche nach Umspannanlagen in dem du den namen der Station oder Teile davon eingibst')


def echo(bot, update):
    """Echo the user message."""
    Stations = localdb.getLinkbyname(update.message.text)
    print(update.message.text)
    if len(Stations) == 0:
        update.message.reply_text(
            "{}? Konnte leider nicht gefunden werden".format(update.message.text)
        )
    elif len(Stations) > 10:
        update.message.reply_text(
            "Mehr als 10 Stationen gefunden. Bitte versuch es präziser"
        )
    elif len(Stations) > 1:
        update.message.reply_text(
            "Mehr als eine Station gefunden"
        )
        for station in Stations:
            update.message.reply_text(
                "Station: {} \nGooglelink:{} \nWazeLink:{}".format(str(station[0]), str(station[1]), str(station[2]))
            )
    else:
        for station in Stations:
            update.message.reply_text(
                "Station: {} \nGooglelink:{} \nWazeLink:{}".format(str(station[0]), str(station[1]), str(station[2]))
            )
    mybots[update.message.chat_id] = bot


def main():
    """Start the bot."""

    print("start bot")
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN_TELEGRAM)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("hilfe", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

    i = 1
    while True:

        time.sleep(60)

        continue

        # kein beep
        for id, bot in mybots.items():
            i += 1
            bot.send_message(id, text="Beep! " + str(i))

    updater.idle()


if __name__ == "__main__":
    main()
