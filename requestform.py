from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    parameters = State()

class Figures(StatesGroup):
    parameters = State()

class Figure(StatesGroup):
    parameters = State()
