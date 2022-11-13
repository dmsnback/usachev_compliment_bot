from telebot import TeleBot, types

from compliments import compliment

api_token = '5691610356:AAGfXU20F7sAwqc5F7qC06dp_8-m0VgmAzc'
bot = TeleBot(api_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=1
    )
    start = types.KeyboardButton(
        'Получить комплимент'
    )
    markup.add(start)
    bot.send_message(
        message.chat.id, f'Привет! {message.from_user.first_name}\n'
        'Я каждый день буду отправлять тебе '
        'коплимент от Руслана Усачева.',
        reply_markup=markup
    )


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Получить комплимент':
        bot.send_message(
            message.chat.id,
            compliment()
        )


bot.polling(none_stop=True)
