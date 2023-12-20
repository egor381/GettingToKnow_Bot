import telebot
from telebot import types
from info import *

token = "token"
bot = telebot.TeleBot(token)


def response_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(
        types.KeyboardButton("📇 Визитная карточка"),
        types.KeyboardButton("📷 Фото персонажа")
    )

    bot.send_message(message.chat.id,
                     text = f"Привет {message.from_user.first_name}, я бот-визитка, и я могу тебе рассказать о персонаже"
                            f"напиши /help, чтобы узнать что я могу",
                     reply_markup = markup
                     )


def response_help(message):
    bot.send_message(message.chat.id,
                     parse_mode = "MarkdownV2",
                     text = "Для данного бота вы можете использовать одну из команд:\n\n" +
                            commands_to_string()
                     )


def response_about(message):
    bot.send_message(message.chat.id,
                     parse_mode = "MarkdownV2",
                     text = "_Визитная карточка персонажа_\n\n" +
                            hobbies_to_string()
                     )

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Да", callback_data = 'фото персонажа'),
        types.InlineKeyboardButton("Нет", callback_data = 'нет, спасибо')
    )

    bot.send_message(message.chat.id,
                     text = "Желаете получить фото персонажа?",
                     reply_markup = markup
                     )


def response_photo(message):
    bot.send_photo(message.chat.id,
                   caption = "Фотография персонажа",
                   photo = get_photo()
                   )

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Да", callback_data = 'визитная карточка'),
        types.InlineKeyboardButton("Нет", callback_data = 'нет, спасибо')
    )

    bot.send_message(message.chat.id,
                     text = "Желаете получить визитную карточку персонажа?",
                     reply_markup = markup
                     )


def response_finish(message):
    bot.send_message(message.chat.id,
                     text = "Хорошего вам настроения 🙃"
                     )


commands = [
    {
        'command': '/start',
        'description': 'начало работы',
        'keywords': ['старт'],
        'handler': response_start
    },
    {
        'command': '/help',
        'description': 'перечень, поддерживаемых команд',
        'keywords': ['помоги мне'],
        'handler': response_help
    },
    {
        'command': '/about',
        'description': 'визитная карточка персонажа',
        'keywords': ['визитная карточка', 'визитка', 'информация'],
        'handler': response_about
    },
    {
        'command': '/photo',
        'description': 'фотография персонажа',
        'keywords': ['фото персонажа', 'фото'],
        'handler': response_photo
    },
    {
        'command': None,
        'description': None,
        'keywords': ['нет, спасибо', 'спасибо'],
        'handler': response_finish
    }
]


def commands_to_string():
    result = ''
    for command in commands:
        if command['command'] and command['description']:
            result += f"*{command['command']}* \- {command['description']}\n"
    return result


def process_message(message, text):
    for command in commands:
        handler = None
        if command['command'] == text.lower():
            handler = command['handler']
        else:
            keywords = command['keywords']
            for keyword in keywords:
                if keyword in text.lower():
                    handler = command['handler']
        if handler:
            handler(message)


@bot.message_handler(content_types = ['text'])
def text_message(message):
    process_message(message, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    process_message(call.message, call.data)
    bot.answer_callback_query(call.id)


menu_commands = []
for command in commands:
    if command['command'] and command['description']:
        menu_commands.append(telebot.types.BotCommand(command['command'], command['description']))
bot.set_my_commands(menu_commands)
bot.polling(non_stop = True)
