from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from Configs import translations, get_available_languages


class SettingsCallback:
    def __init__(self):
        self.generate_main_inline()
        self.generate_language_inline()

    def generate_main_inline(self):
        self.main_inline_data = CallbackData("button", "value")

        self.main_inline = InlineKeyboardMarkup(row_width=2)
        self.main_inline.insert(
            InlineKeyboardButton(
                text=translations.get('callbacks.keyboards.settings.language'),
                callback_data=self.main_inline_data.new(
                    value='language'
                ))
        )

    def generate_language_inline(self):
        self.language_inline_data = CallbackData("button", "value")

        self.language_inline = InlineKeyboardMarkup(row_width=2)
        for language in get_available_languages():
            self.language_inline.insert(
                InlineKeyboardButton(
                    text=language,
                    callback_data=self.language_inline_data.new(
                        value=language.lower()
                    ))
            )
