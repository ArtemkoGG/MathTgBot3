from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("quadratic_equations"))
async def quadratic_equations(message: Message):
    await message.answer("Введіть коефіцієнти квадратного рівняння (a, b, c)")
    return

    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        await.message.answer(f"Перший корінь - {x1}, Другий корінь - {x2}")


