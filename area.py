from commands import AREA
from aiogram.fsm.context import FSMContext
from requestform import Area
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
    builder.add(InlineKeyboardButton(text="Прямокутник", callback_data="a_figures_rectangle"))
    builder.add(InlineKeyboardButton(text="Трапеція", callback_data="a_figures_trapeze"))

    builder.adjust(1)

    await message.answer("Площу якої фігури в бажаєте визначити?", reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("a_figures_"))
async def solve_area(calback: CallbackQuery, state: FSMContext):
    global FIGURES

    figures = calback.data.split("_")[-1]
    await calback.message.answer(f"Ви обрали фігуру {figures}")
    await state.set_state(Area.parameters)
    FIGURES = figures

    if figures == "triangle":
        await calback.message.answer(f"Введіть сторони Трикутника: a b c")

    elif figures == "square":
        await calback.message.answer(f"Введіть сторону Квадрата: a")

    elif figures == "circle":
        await calback.message.answer(f"Введіть радіус кола: r")

    elif figures == "rectangle":
        await calback.message.answer(f"Введіть сторони Прямокутника: a b")

    elif figures == "trapeze":
        await calback.message.answer(f"Введіть основи та висоту Трапеції: a b h")


@router.message(Area.parameters)
async def solve_perimetr(message: Message, state: FSMContext):
    data: dict = await state.update_data(parameters=message.text)

    if FIGURES == "triangle":
        a, b, c = data['parameters'].split(" ")
        a = int(a)
        b = int(b)
        c = int(c)

        s = (a + b + c) / 2
        s = int(s)
        S = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if FIGURES == "square":
        a = int(data['parameters'])
        S = a ** 2

    if FIGURES == "circle":
        r = int(data['parameters'])
        S = math.pi * r ** 2

    if FIGURES == "rectangle":
        a, b = data['parameters'].split(" ")
        a = int(a)
        b = int(b)
        S = a * b

    if FIGURES == "trapeze":
        a, b, h = data['parameters'].split(" ")
        a = int(a)
        b = int(b)
        h = int(h)
        S = ((a + b) * h) / 2

    await message.answer(f"Площа {FIGURES} = {S}")
    await state.clear()
