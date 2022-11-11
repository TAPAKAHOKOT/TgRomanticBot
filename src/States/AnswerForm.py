from aiogram.dispatcher.filters.state import State, StatesGroup


class AnswerForm(StatesGroup):
    answer = State()
