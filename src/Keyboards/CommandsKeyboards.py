from aiogram import types

from Configs import translations


class CommandsKeyboards:
    @staticmethod
    def get_main_keyboard() -> types.ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start.add(
            types.KeyboardButton(text=''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.get-message')),
            types.KeyboardButton(text=''),
        )

        return start
