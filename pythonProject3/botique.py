import telegram
from telegram.ext import CommandHandler
import logging
from telegram.ext import Updater
TOKEN='5792313266:AAFXdajF50qnnTei5HfrCn28p1MnsDG6Mbs'
bot=telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
def start(update, context):
     context.bot.send_message(chat_id=update.effective_chat.id,
     text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def echo(update, context):
    text = '*Відлуння*\n'+update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
def photka(update, context):
    text='Не розбираюсь в мистецтві...'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
def vidos(update, context):
    text=':D Лаха'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
photo_handler = MessageHandler(Filters.photo & (~Filters.command), photka)
video_handler = MessageHandler(Filters.video & (~Filters.command), vidos)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(video_handler)
updater.start_polling()