import logging
from msilib.schema import Upgrade
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from finvizfinance.screener.overview import Overview
from finvizfinance.quote import finvizfinance
import pandas as pd
from twilio.rest import Client
from telethon import TelegramClient, events, sync
from tkinter import *
from tkinter import messagebox
import pandas as pd



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def checkAlgo(update, context):
    foverview = Overview()
    foverview._set_signal(signal="Upgrades")
    filters_dict = {'Index':'S&P 500','Sector':'Any' ,'Market Cap.': '+Mid (over $2bln)' , 'Average Volume': 'Over 500K' , 'Average True Range': 'Over 0.75', 'Pattern': 'Channel (Strong)'}
    foverview.set_filter(filters_dict=filters_dict)
    data = foverview.screener_view()
    
    if data is  None:
        update.message.reply_text("The are No Stock for the algo")
    else:
        for d in data.values:
            StockTicker = d[0]
            StockCompany = d[1]
            StockSector = d[2]
            StockCountry = d[4]
            message = f'The Stock {StockCompany} with the Symbol {StockTicker} from The {StockSector} Sector can be Good For The Swing algorightm '
            update.message.reply_text(str(message))
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5586549693:AAEImZ_Fr2nplPMrIDp-Q26_1p81tWUiZ5Y", use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("algo",checkAlgo))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling() # Start the Bot
    updater.idle()


if __name__ == '__main__':
    main()