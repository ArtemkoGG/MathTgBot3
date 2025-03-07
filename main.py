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
from quadratic_equations import router as qr
from perimetr import router as pr
from area import router as ar

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()
dp.include_router(qr)
dp.include_router(pr)
dp.include_router(ar)


@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        f"Привіт, {html.bold(message.from_user.full_name)}!\n\n"
        "Я математичний бот Артема який допоможе з різними задачами \n\n"
        "Ось, що я можу:\n"
        "1. Квадратні рівняння.\n"
        "2. Обчислити периметр фігур\n"
        "3. Обчислити площу фігур"
    )


async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="1.Зaпуск ботa"),
            BotCommand(
                command="quadratic_equations", description="2.Квадратні рівняння"
            ),
            BotCommand(command="perimetr", description="3.Визначити периметр"),
            BotCommand(command="area", description="4.Визначити площу"),
        ]
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())