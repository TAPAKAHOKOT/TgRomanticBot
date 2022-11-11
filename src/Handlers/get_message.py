from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode

from Configs import translations
from Settings import settings
from Tables import User
from src.Services import MessagesService


@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.get-message')))
async def write_to_dev_message(message: types.Message, user: User):
    random_message = await MessagesService.get_random_message(
        user.id,
        settings.limits['hours'],
        settings.limits['messages']
    )

    if random_message is None:
        await message.answer('Нет доступных сообщений')
        return

    if isinstance(random_message, str):
        await message.answer(f'Следующее сообщение будет доступно через {random_message}')
        return

    await settings.bot.copy_message(
        from_chat_id=random_message['chat_id'],
        chat_id=message.chat.id,
        message_id=random_message['message_id']
    )

    try:
        if settings.resend_to:
            for chat_id in settings.resend_to:
                await settings.bot.send_message(
                    chat_id=chat_id,
                    text=f'Пользователь [ <a href=\'https://t.me/{user.username}\'>{user.username}</a> ] [<a href=\'https://web.telegram.org/k/#{message.chat.id}\'>{message.chat.id}</a>] получил сообщение',
                    parse_mode=ParseMode.HTML
                )
                await settings.bot.copy_message(
                    from_chat_id=random_message['chat_id'],
                    chat_id=chat_id,
                    message_id=random_message['message_id']
                )
    except Exception as e:
        pass
