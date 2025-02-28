from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import QUADRATIC
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from requestform import Form
router = Router()




@router.message(Command(QUADRATIC))
async def quadratic_equations(message: Message, state: FSMContext):
    await state.set_state(Form.parameters)
    await message.answer("Введіть коефіцієнти квадратного рівняння (a b c)")


@router.message(Form.parameters)
async def solve_quadratic(message: Message, state: FSMContext):
    await state.update_data(parameters=message.text)

    data: dict[str, str] = await state.get_data()

    coefficients = data["parameters"].split()
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        await message.answer(f"Корені рівняння:\nx1 = {x1}\nx2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        await message.answer(f"Рівняння має корінь: x = {x}")
    else:
        await message.answer("Рівняння не має коренів")

    await state.clear()
