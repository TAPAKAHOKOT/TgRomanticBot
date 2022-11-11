from aiogram import types
from aiogram.types import ParseMode

from Settings import settings
from Tables import User


@settings.dp.message_handler(content_types=['any'])
async def save_any_message(message: types.Message, user: User):
    try:
        if settings.resend_to:
            for chat_id in settings.resend_to:
                await settings.bot.send_message(
                    chat_id=chat_id,
                    text=f'Пользователь [ <a href=\'https://t.me/{user.username}\'>{user.username}</a> ] [<a href=\'https://web.telegram.org/k/#{message.chat.id}\'>{message.chat.id}</a>] получил сообщение',
                    parse_mode=ParseMode.HTML
                )
                await settings.bot.copy_message(
                    from_chat_id=message.chat.id,
                    chat_id=chat_id,
                    message_id=message.message_id
                )
    except Exception:
        pass
