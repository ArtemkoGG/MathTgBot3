import math
from commands import PERIMETR
from aiogram.fsm.context import FSMContext
from requestform import Perimetr
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
FIGURE = None


@router.message(Command(PERIMETR))
async def perimetr(message: Message):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="Трикутник", callback_data="p_figures_triangle"))
    builder.add(InlineKeyboardButton(text="Квадрат", callback_data="p_figures_square"))
    builder.add(InlineKeyboardButton(text="Коло", callback_data="p_figures_circle"))
    builder.add(InlineKeyboardButton(text="Прямокутник", callback_data="p_figures_rectangle"))
    builder.add(InlineKeyboardButton(text="Трапеція", callback_data="p_figures_trapeze"))


    builder.adjust(1)

    await message.answer("Периметр якої фігури в бажаєте визначити?", reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("p_figures_"))
async def solve_perimetr(calback: CallbackQuery, state: FSMContext):
    global FIGURE

    figure = calback.data.split("_")[-1]
    await calback.message.answer(f"Ви обрали фігуру {figure}")
    await state.set_state(Perimetr.parameters)
    FIGURE = figure

    if figure == "triangle":
        await calback.message.answer(f"Введіть сторони Трикутника: a b c")

    elif figure == "square":
        await calback.message.answer(f"Введіть сторону Квадрата: a")

    elif figure == "circle":
        await calback.message.answer(f"Введіть радіус Кола: r")

    elif figure == "rectangle":
        await calback.message.answer(f"Введіть сторони Прямокутника: a b")

    elif figure == "trapeze":
        await calback.message.answer(f"Введіть сторони Трапеції: a b c d")


@router.message(Perimetr.parameters)
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

    if FIGURE == "rectangle":
        a, b = data['parameters'].split(" ")
        a = int(a)
        b = int(b)
        P = 2 * (a + b)

    if FIGURE == "trapeze":
        a, b, c, d = map(int, data['parameters'].split())
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        P = a + b + c + d

    await message.answer(f"Периметр {FIGURE} = {P}")
    await state.clear()


