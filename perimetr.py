from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import PERIMETR
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from requestform import Form
router = Router()


@router.message(Command(PERIMETR))
async def perimetr(message: Message, state: FSMContext):
    await state.set_state(Form.parameters)
    await message.answer("Периметр якої фігури в бажаєте визначити?\n 1 - Трикутник\n 2 - Квадрат\n 3 - Прямокутник\n 4 - Коло")

@router.message(Form.parameters)
async def solve_perimetr(message: Message, state: FSMContext):
    await state.update_data(parameters=message.text)
    data: dict[str, str] = await state.get_data()

    choice = data["parameters"]

    if choice == "1":
        await state.set_state(Form.parameters)
        await message.answer("Введіть 3 сторони трикутника через пробіл (a b c):")
        coefficients = data["parameters"].split()
        a = float(coefficients[0])
        b = float(coefficients[1])
        c = float(coefficients[2])

        perimetr_triangle = a + b + c
        await message.answer(f"Ось периметр трикутника {perimetr_triangle}")

    elif choice == "2":
        await state.set_state(Form.parameters)
        await message.answer("Введіть довжину сторони квадрата:")
    elif choice == "3":
        await state.set_state(Form.parameters)
        await message.answer("Введіть довжини двох сторін прямокутника через пробіл (a b):")
    elif choice == "4":
        await state.set_state(Form.parameters)
        await message.answer("Введіть радіус кола:")
    else:
        await message.answer("Невірний вибір. Будь ласка, виберіть 1, 2, 3 або 4.")


