from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import PERIMETR
from aiogram.fsm.context import FSMContext
from requestform import Form
from random import randint
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
router = Router()


@router.message(Command(PERIMETR))
async def perimetr(message: Message, state: FSMContext):
    await state.set_state(Form.parameters)
    await message.answer("Периметр якої фігури в бажаєте визначити?")

def inline_learn_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text = "Трикутник"
        )
    )

    builder.row(InlineKeyboardButton(text="Трикутник", callback_data="value_random"))
    builder.add(InlineKeyboardButton(text="10", callback_data="value_10"))

    return builder.as_markup()

@router.message(Form.parameters)
async def solve_perimetr(message: Message, state: FSMContext):
    await state.update_data(parameters=message.text)
