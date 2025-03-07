from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    parameters = State()

class Area(StatesGroup):
    parameters = State()

class Perimetr(StatesGroup):
    parameters = State()
