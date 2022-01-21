import telebot

from api import BlockchainRates
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

rates = BlockchainRates()

@bot.message_handler(commands="start")
def start_handler(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="Напишите символьное обозначение криптовалюты")


@bot.message_handler(content_types=["text"])
def message_handler(message: telebot.types.Message):
    answer = rates.get(message.text.upper()) or "Такая криптовалюта не найдена!"

    bot.send_message(chat_id=message.chat.id, text=answer)


bot.polling(none_stop=True)