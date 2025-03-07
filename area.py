from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import AREA
from aiogram.fsm.context import FSMContext
from requestform import Figure
from random import randint
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import math

router = Router()

FIGURES = None


@router.message(Command(AREA))
async def area(message: Message):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="Трикутник", callback_data="a_figures_triangle"))
    builder.add(InlineKeyboardButton(text="Квадрат", callback_data="a_figures_square"))
    builder.add(InlineKeyboardButton(text="Коло", callback_data="a_figures_circle"))

    await message.answer("Площу якої фігури в бажаєте визначити?", reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("a_figures_"))
async def solve_area(calback: CallbackQuery, state: FSMContext):
    global FIGURES

    figures = calback.data.split("_")[-1]
    await calback.message.answer(f"Ви обрали фігуру {figures}")
    await state.set_state(Figure.parameters)
    FIGURES = figures

    if figures == "triangle":
        await calback.message.answer(f"Введіть сторони Трикутника: a b c")

    elif figures == "square":
        await calback.message.answer(f"Введіть сторону Квадрата: a")

    elif figures == "circle":
        await calback.message.answer(f"Введіть радіус кола: r")


@router.message(Figure.parameters)
async def solve_perimetr(message: Message, state: FSMContext):
    data: dict = await state.update_data(parameters=message.text)

    if FIGURES == "triangle":
        a, b, c = data['parameters'].split(" ")
        s = (a + b + c) / 2
        S = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if FIGURES == "square":
        a = int(data['parameters'])
        S = a ** 2

    if FIGURES == "circle":
        r = int(data['parameters'])
        S = math.pi * r ** 2

    await message.answer(f"Площа {FIGURES} = {S}")
    await state.clear()
