from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject, CommandStart
import random
from aiogram.methods.send_message import SendMessage
import app.keyboards as kb

router = Router()

bot = Bot(token="7469695246:AAEGMd9TlZdvpn0bPogqGiBqF7BCiyV5eZc")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>!\nЭтот бот может загадать тебе рандомное число,"
        f" на этом пока всё. "
        f"Разработчик расширяет функционал и фиксит баги практически каждый день"
        f"\nВопросы и предложения:\n@klReee\nDiscord:bavae#1226\n",
        reply_markup=kb.main,
        parse_mode="HTML",
    )


@router.message(Command("games"))
async def games(message: Message):
    await message.answer(
        f"Вот список игр и как в них играть:\n1. <b>команда</b>: '/game 1-20'\nЭто значит, что бот "
        f"отправит рандомное число от 1 до 20. Сюда можно писать любые числа и цифры\n"
        f"Пока на этом всё. Скоро будут новые игры",
        parse_mode="HTML",
    )


@router.message(Command("info_prog"))
async def info_prog(message: Message):
    await message.answer(f"Я же сказал, скоро...")
    await message.answer(f"Скоро...")


@router.message(Command("game"))
async def send_randint(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)
    await message.reply("Твоё рандомное число...")
    await message.answer("Иии...")
    await message.answer("Барабанная дробь...")
    await message.answer(f"{rnum}")


@router.message(Command("help"))
async def helps(message: Message):
    await message.answer(
        f"Вот список команд:\n/game - как играть\n/info_prog - где и как обучаться программированию бесплатно"
        f"(скоро будет эта функция)\n/help - список команд"
    )


@router.message()
async def games_also(message: Message):
    if message.text == "игры":
        await message.answer(
            f"Вот список игр и как в них играть:\n1. <b>команда</b>: '/game 1-20'\nЭто значит, что бот "
            f"отправит рандомное число от 1 до 20. Сюда можно писать любые числа и цифры\n"
            f"Пока на этом всё. Скоро будут новые игры",
            parse_mode="HTML",
            reply_markup=kb.next_sec123,
        )


@router.message(Command("next"))
async def next_game(message: Message):
    await message.answer("tets")


@router.callback_query(F.data == "next")
async def callback_one(callback: CallbackQuery):
    await callback.answer("молодец!")
    await callback.message.answer(
        "Для примера, напиши команду '/game 1-100' ", reply_markup=kb.nexti
    )


# @router.callback_query(Command.filter(function='next'))
# async def nexter(query: )


@router.callback_query(lambda query: query.data == "back")
async def call_back(callback: CallbackQuery):
    await callback.answer("/game 1-20")
    await callback.message.answer("test", reply_markup=kb.backi)
    bot.send_message(chat_id=CallbackQuery.message.chat.id, text="cajnnnncel")


@router.message(Command("test"))
async def mainser(message: Message):
    await message.answer("это мой(твой) тесат")


@router.message(Command("info"))
async def info_command(message: Message):
    await message.answer("tets")


# router.message()
# async def backs(message: Message):
# message.text == 'НАЗАД' if reply_markup = kb.main else message.answer('LOREM IMSUM')
#       await message.answer('ты решил вернуться...')


@router.message()
async def tests(message: Message):
    if message.text == "вернуться":
        await message.answer("tests of me(my tests)", reply_markup=kb.main)


@router.message()
async def playser(message: Message, command: CommandObject):
    if message.text == "играть":
        a, b = [int(n) for n in command.args.split("-")]
        rnum = random.randint(a, b)
        await message.reply("Твоё рандомное число...")
        await message.answer("Иии...")
        await message.answer("Барабанная дробь...")
        await message.answer(f"{rnum}")


@router.message()
async def marunaa(message: Message):
    if message.text.lower == "тест123":
        await message.answer("это тест", reply_markup=kb.testt)


@router.message(F.text == "тестназ")
async def rmer(message: Message):
    await message.answer("да да...")
