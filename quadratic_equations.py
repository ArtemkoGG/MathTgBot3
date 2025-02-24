from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("quadratic_equations"))
async def quadratic_equations(message: Message):
    await message.answer("Введіть коефіцієнти квадратного рівняння (a, b, c)")
    return

@router.message()
async def solve_quadratic(message: Message):
        coefficients = message.text.split()
        a = float(coefficients[0])
        b = float(coefficients[1])
        c = float(coefficients[2])

        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            await message.answer(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
        elif D == 0:
            x = -b / (2 * a)
            await message.answer(f"Рівняння має корінь: x = {x}")
        else:
            await message.answer("Рівняння не має коренів")


