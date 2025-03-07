from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import PERIMETR
from aiogram.fsm.context import FSMContext
from requestform import Figures
from random import randint
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import math

router = Router()

FIGURE = None


@router.message(Command(PERIMETR))
async def perimetr(message: Message):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="Трикутник", callback_data="p_figures_triangle"))
    builder.add(InlineKeyboardButton(text="Квадрат", callback_data="p_figures_square"))
    builder.add(InlineKeyboardButton(text="Коло", callback_data="p_figures_circle"))

    await message.answer("Периметр якої фігури в бажаєте визначити?", reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("p_figures_"))
async def solve_perimetr(calback: CallbackQuery, state: FSMContext):
    global FIGURE

    figure = calback.data.split("_")[-1]
    await calback.message.answer(f"Ви обрали фігуру {figure}")
    await state.set_state(Figures.parameters)
    FIGURE = figure

    if figure == "triangle":
        await calback.message.answer(f"Введіть сторони Трикутника: a b c")

    elif figure == "square":
        await calback.message.answer(f"Введіть сторону Квадрата: a")

    elif figure == "circle":
        await calback.message.answer(f"Введіть радіус кола: r")


@router.message(Figures.parameters)
async def solve_perimetr(message: Message, state: FSMContext):
    data: dict = await state.update_data(parameters=message.text)

    if FIGURE == "triangle":
        a, b, c = data['parameters'].split(" ")
        P = int(a) + int(b) + int(c)

    if FIGURE == "square":
        a = data['parameters'].split(" ")
        P = int(a[0]) * 4

    if FIGURE == "circle":
        r = int(data['parameters'])
        P = 2 * math.pi * r

    await message.answer(f"Периметр {FIGURE} = {P}")
    await state.clear()


