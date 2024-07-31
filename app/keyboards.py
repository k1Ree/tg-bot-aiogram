from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="игры"),
        ],
        [
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Отправить гео", request_location=True),
            KeyboardButton(
                text="Сделать голосование", request_poll=KeyboardButtonPollType()
            ),
        ],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выбери действие меню...",
)


next_sec123 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="next")],
        [InlineKeyboardButton(text="назад", callback_data="back")],
    ]
)

backi = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="вернуться")]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Вернуться назад...",
)

nexti = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="играть")]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Click! Click! Click!",
)

testt = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="тестназ")]])
