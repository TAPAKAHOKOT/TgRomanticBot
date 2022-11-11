from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


class AnswerCallback:
    @staticmethod
    def get_answer_inline_data():
        return CallbackData("answer_message", "username", "chat_id", "reply_message_id")

    @staticmethod
    def get_answer_inline(
            username: str,
            chat_id: int,
            reply_message_id: int
    ):
        inline_data = AnswerCallback.get_answer_inline_data()

        inline = InlineKeyboardMarkup(row_width=1)
        inline.insert(
            InlineKeyboardButton(
                text='Ответить',
                callback_data=inline_data.new(
                    username=username,
                    chat_id=chat_id,
                    reply_message_id=reply_message_id
                ))
        )
        return inline

    @staticmethod
    def get_cancel_inline_data():
        return CallbackData("cancel")

    @staticmethod
    def get_cancel_inline():
        inline_data = AnswerCallback.get_cancel_inline_data()

        inline = InlineKeyboardMarkup(row_width=2)
        inline.insert(
            InlineKeyboardButton(
                text='Отмена',
                callback_data=inline_data.new())
        )
        return inline
