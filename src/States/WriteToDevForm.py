from aiogram.dispatcher.filters.state import State, StatesGroup


class WriteToDevForm(StatesGroup):
    white_to_dev = State()
