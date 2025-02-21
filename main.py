import asyncio
import logging
import sys

from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.types import BotCommand


load_dotenv()

TOKEN = getenv("TOKEN")
dp = Dispatcher()



@dp.message(CommandStart())
async def command_start(message: Message) -> None:



    await message.answer(
        f"Привіт, {html.bold(message.from_user.full_name)}!\n\n"
        "Я математичний бот Артема який допоможе з різними задачами \n\n"
        "Ось, що я можу:\n"
        "1. Квадратні рівняння.\n"
        "2. Обчислити НСД\n"
        "3. Обчислити НСК\n"
        "4. Обчислити периметр фігур\n"
        "5. Обчислити площу фігур"

    )



async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="1.Зaпуск ботa"),
            BotCommand(command="quadratic_equations", description="2.Квадратні рівняння"),
            BotCommand(command="nsd", description="3.Визначити НСД"),
            BotCommand(command="perimetr", description="4.Визначити периметр"),
            BotCommand(command="area", description="5.Визначити площу"),
        ]
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())