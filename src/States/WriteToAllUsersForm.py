from aiogram.dispatcher.filters.state import State, StatesGroup


class WriteToAllUsersForm(StatesGroup):
    write_to_all_users = State()
