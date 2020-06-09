from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackQueryHandler
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from aparser.models import Message
from aparser.models import Profile
from aparser.models import Product

# `callback_data` -- это то, что будет присылать TG при нажатии на каждую кнопку.
# Поэтому каждый идентификатор должен быть уникальным
CALLBACK_BUTTON1_PRICE = "callback_button1_price"
CALLBACK_BUTTON2_PRICE = "callback_button2_price"
CALLBACK_BUTTON10_MORE = "callback_button10_more"
CALLBACK_BUTTON1_BACK = "callback_button1_back"
CALLBACK_BUTTON2_BACK = "callback_button1_back"
CALLBACK_BUTTON3_BACK = "callback_button1_back"
CALLBACK_BUTTON5_PRICE = "callback_button5_price"
CALLBACK_BUTTON6_PRICE = "callback_button6_price"
CALLBACK_BUTTON7_PRICE = "callback_button7_price"
CALLBACK_BUTTON8_PRICE = "callback_button8_price"
CALLBACK_BUTTON9_PRICE = "callback_button9_price"
CALLBACK_BUTTON10_PRICE = "callback_button10_price"
CALLBACK_BUTTON11_PRICE = "callback_button11_price"
CALLBACK_BUTTON12_PRICE = "callback_button12_price"
CALLBACK_BUTTON13_PRICE = "callback_button13_price"
CALLBACK_BUTTON14_PRICE = "callback_button14_price"
CALLBACK_BUTTON15_PRICE = "callback_button15_price"
CALLBACK_BUTTON16_PRICE = "callback_button16_price"
CALLBACK_BUTTON1_ROOM = "callback_button1_room"
CALLBACK_BUTTON2_ROOM = "callback_button2_room"
CALLBACK_BUTTON3_ROOM = "callback_button3_room"
CALLBACK_BUTTON4_ROOM = "callback_button4_room"
CALLBACK_BUTTON5_ROOM = "callback_button5_room"
CALLBACK_BUTTON6_ROOM = "callback_button6_room"
CALLBACK_BUTTON_HIDE_KEYBOARD = "callback_button9_hide"
CALLBACK_BUTTON1_MORE = "callback_button1_more"
CALLBACK_BUTTON2_MORE = "callback_button2_more"
CALLBACK_BUTTON3_MORE = "callback_button3_more"
CALLBACK_BUTTON3_URL = "callback_button3_url"

TITLES = {
    CALLBACK_BUTTON1_PRICE: "0-1.000.000",
    CALLBACK_BUTTON2_PRICE: "1.000.000-2.000.000",
    CALLBACK_BUTTON10_MORE: "Ещё ➡️",
    CALLBACK_BUTTON1_BACK: "Назад ⬅️",
    CALLBACK_BUTTON2_BACK: "Назад ⬅️",
    CALLBACK_BUTTON3_BACK: "Назад ⬅️",
    CALLBACK_BUTTON5_PRICE: "2.000.000-3.000.000",
    CALLBACK_BUTTON6_PRICE: "3.000.000-4.000.000",
    CALLBACK_BUTTON7_PRICE: "4.000.000-5.000.000",
    CALLBACK_BUTTON8_PRICE: "5.000.000-6.000.000",
    CALLBACK_BUTTON9_PRICE: "6.000.000-7.000.000",
    CALLBACK_BUTTON10_PRICE: "7.000.000-8.000.000",
    CALLBACK_BUTTON11_PRICE: "8.000.000-10.000.000",
    CALLBACK_BUTTON12_PRICE: "10.000.000-12.000.000",
    CALLBACK_BUTTON13_PRICE: "12.000.000-15.000.000",
    CALLBACK_BUTTON14_PRICE: "15.000.000-20.000.000",
    CALLBACK_BUTTON15_PRICE: "20.000.000-30.000.000",
    CALLBACK_BUTTON16_PRICE: "30.000.000-50.000.000",
    CALLBACK_BUTTON_HIDE_KEYBOARD: "Спрятать клавиатуру",
    CALLBACK_BUTTON1_ROOM: "Студия",
    CALLBACK_BUTTON2_ROOM: "1 комната",
    CALLBACK_BUTTON3_ROOM: "2 комнаты",
    CALLBACK_BUTTON4_ROOM: "3 комнаты",
    CALLBACK_BUTTON5_ROOM: "4 комнаты",
    CALLBACK_BUTTON6_ROOM: "5 комнат",
    CALLBACK_BUTTON1_MORE: "Ещё 5 ⚡️",
    CALLBACK_BUTTON2_MORE: "Ещё 5 ⚡️",
    CALLBACK_BUTTON3_MORE: "Ещё 10 ⚡️",
    CALLBACK_BUTTON3_URL: "Ссылка 🏢"
}


def get_base_inline_keyboard():
    """ Получить клавиатуру для сообщения
        Эта клавиатура будет видна под каждым сообщением, где её прикрепили
    """
    # Каждый список внутри `keyboard` -- это один горизонтальный ряд кнопок
    keyboard = [
        # Каждый элемент внутри списка -- это один вертикальный столбец.
        # Сколько кнопок -- столько столбцов
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_PRICE], callback_data=CALLBACK_BUTTON1_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_PRICE], callback_data=CALLBACK_BUTTON2_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_PRICE], callback_data=CALLBACK_BUTTON5_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_PRICE], callback_data=CALLBACK_BUTTON6_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_PRICE], callback_data=CALLBACK_BUTTON7_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_PRICE], callback_data=CALLBACK_BUTTON8_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_PRICE], callback_data=CALLBACK_BUTTON9_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HIDE_KEYBOARD], callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_MORE], callback_data=CALLBACK_BUTTON10_MORE),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard2():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_PRICE], callback_data=CALLBACK_BUTTON10_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_PRICE], callback_data=CALLBACK_BUTTON11_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON12_PRICE], callback_data=CALLBACK_BUTTON12_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON13_PRICE], callback_data=CALLBACK_BUTTON13_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_PRICE], callback_data=CALLBACK_BUTTON14_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_BACK], callback_data=CALLBACK_BUTTON1_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard3():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_ROOM], callback_data=CALLBACK_BUTTON1_ROOM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_ROOM], callback_data=CALLBACK_BUTTON2_ROOM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_ROOM], callback_data=CALLBACK_BUTTON3_ROOM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_ROOM], callback_data=CALLBACK_BUTTON4_ROOM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_ROOM], callback_data=CALLBACK_BUTTON5_ROOM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_ROOM], callback_data=CALLBACK_BUTTON6_ROOM, )
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_BACK], callback_data=CALLBACK_BUTTON2_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard4():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_MORE], callback_data=CALLBACK_BUTTON1_MORE),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard5():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_MORE], callback_data=CALLBACK_BUTTON2_MORE),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard6():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard7():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_URL], callback_data=CALLBACK_BUTTON3_URL),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback_handler(update: Update, context: CallbackContext):
    """ Обработчик ВСЕХ кнопок со ВСЕХ клавиатур
    """
    global rl, room, lprice, gprice
    query = update.callback_query
    data = query.data

    # Обратите внимание: используется `effective_message`
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBACK_BUTTON10_MORE:
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2(),
        )
    elif data == CALLBACK_BUTTON1_BACK:
        # Показать предыдущий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON2_BACK:
        # Показать предыдущий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text="Выберите диапазон цен",
            reply_markup=get_keyboard2(),
        )
    elif data == CALLBACK_BUTTON_HIDE_KEYBOARD:
        # Спрятать клавиатуру
        # Работает только при отправке нового сообщение
        # Можно было бы отредактировать, но тогда нужно точно знать что у сообщения не было кнопок
        context.bot.send_message(
            chat_id=chat_id,
            text="Спрятали клавиатуру\n\nНажмите /buy чтобы вернуть её обратно",
            reply_markup=ReplyKeyboardRemove(),
        )

    elif data in (CALLBACK_BUTTON1_PRICE, CALLBACK_BUTTON2_PRICE, CALLBACK_BUTTON5_PRICE, CALLBACK_BUTTON6_PRICE,
                  CALLBACK_BUTTON7_PRICE, CALLBACK_BUTTON8_PRICE, CALLBACK_BUTTON9_PRICE, CALLBACK_BUTTON10_PRICE,
                  CALLBACK_BUTTON11_PRICE, CALLBACK_BUTTON12_PRICE, CALLBACK_BUTTON13_PRICE, CALLBACK_BUTTON14_PRICE):
        lprice = {
            CALLBACK_BUTTON1_PRICE: 0,
            CALLBACK_BUTTON2_PRICE: 1000000,
            CALLBACK_BUTTON5_PRICE: 2000000,
            CALLBACK_BUTTON6_PRICE: 3000000,
            CALLBACK_BUTTON7_PRICE: 4000000,
            CALLBACK_BUTTON8_PRICE: 5000000,
            CALLBACK_BUTTON9_PRICE: 6000000,
            CALLBACK_BUTTON10_PRICE: 7000000,
            CALLBACK_BUTTON11_PRICE: 8000000,
            CALLBACK_BUTTON12_PRICE: 10000000,
            CALLBACK_BUTTON13_PRICE: 12000000,
            CALLBACK_BUTTON14_PRICE: 15000000,
        }[data]
        gprice = {
            CALLBACK_BUTTON1_PRICE: 1000000,
            CALLBACK_BUTTON2_PRICE: 2000000,
            CALLBACK_BUTTON5_PRICE: 3000000,
            CALLBACK_BUTTON6_PRICE: 4000000,
            CALLBACK_BUTTON7_PRICE: 5000000,
            CALLBACK_BUTTON8_PRICE: 6000000,
            CALLBACK_BUTTON9_PRICE: 7000000,
            CALLBACK_BUTTON10_PRICE: 8000000,
            CALLBACK_BUTTON11_PRICE: 10000000,
            CALLBACK_BUTTON12_PRICE: 12000000,
            CALLBACK_BUTTON13_PRICE: 15000000,
            CALLBACK_BUTTON14_PRICE: 20000000,
        }[data]

        query.edit_message_text(
            text="Выберите кол-во комнат",
            reply_markup=get_keyboard3(),
        )

    elif data in (CALLBACK_BUTTON1_ROOM, CALLBACK_BUTTON2_ROOM, CALLBACK_BUTTON3_ROOM,
                  CALLBACK_BUTTON4_ROOM, CALLBACK_BUTTON5_ROOM, CALLBACK_BUTTON6_ROOM):
        text = 'Предложения на рынке:\n'
        room = {
            CALLBACK_BUTTON1_ROOM: 'Студия',
            CALLBACK_BUTTON2_ROOM: '1-к',
            CALLBACK_BUTTON3_ROOM: '2-к',
            CALLBACK_BUTTON4_ROOM: '3-к',
            CALLBACK_BUTTON5_ROOM: '4-к',
            CALLBACK_BUTTON6_ROOM: '5-к',
        }[data]
        rl = Product.objects.filter(
            price__gte=lprice,
            price__lt=gprice,
            title__contains=f'{room}',
        )
        for e in rl[0:5]:
            text = text + '\n'.join([f'{e.title}:\n{e.url}\n\n'])
        query.edit_message_text(
            text=f'\n{text}',
            reply_markup=get_keyboard4(),
        )

    elif data == CALLBACK_BUTTON1_MORE:
        text = 'Предложения на рынке:\n'

        rl = Product.objects.filter(
            price__gte=lprice,
            price__lt=gprice,
            title__contains=f'{room}',
        )
        for e in rl[5:10]:
            text = text + '\n'.join([f'{e.title}:\n{e.url}\n\n'])
        context.bot.send_message(
            chat_id=chat_id,
            text=f'\n{text}',
            reply_markup=get_keyboard5(),
        )

    elif data == CALLBACK_BUTTON2_MORE:
        text = 'Предложения на рынке:\n'

        rl = Product.objects.filter(
            price__gte=lprice,
            price__lt=gprice,
            title__contains=f'{room}',
        )
        for e in rl[10:15]:
            text = text + '\n'.join([f'{e.title}:\n{e.url}\n\n'])
        context.bot.send_message(
            chat_id=chat_id,
            text=f'\n{text}',
            reply_markup=get_keyboard6(),
        )

    elif data == CALLBACK_BUTTON3_MORE:
        text = 'Предложения на рынке:\n'

        rl = Product.objects.filter(
            price__gte=lprice,
            price__lt=gprice,
            title__contains=f'{room}',
        )
        for e in rl[15:25]:
            text = text + '\n'.join([f'{e.title}:\n{e.url}\n\n'])
        context.bot.send_message(
            chat_id=chat_id,
            text=f'\n{text}',
        )
    elif data == CALLBACK_BUTTON3_URL:
        query.edit_message_text(
            text=current_text

        )


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    m = Message(
        profile=p,
        text=text,
    )
    m.save()


@log_errors
def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    count = Message.objects.filter(profile=p).count()

    update.message.reply_text(
        text=f'У вас {count} сообщений',
    )


@log_errors
def do_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=f'Привет!\n'
             'Список доступных команд есть в меню'
    )


@log_errors
def do_buy(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=f'Выберите диапазон цен',
        reply_markup=get_base_inline_keyboard(),
    )


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # 1 -- правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )
        print(bot.get_me())

        # 2 -- обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        updater.dispatcher.add_handler(CommandHandler("buy", do_buy))
        updater.dispatcher.add_handler(CommandHandler("buy", do_echo))
        updater.dispatcher.add_handler(CommandHandler("count", do_count))
        updater.dispatcher.add_handler(CommandHandler("start", do_start))
        message_handler = MessageHandler(Filters.text, do_echo)
        buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)
        updater.dispatcher.add_handler(message_handler)
        updater.dispatcher.add_handler(buttons_handler)

        # 3 -- запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()
