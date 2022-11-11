from aiogram import types
from aiogram.dispatcher.filters import Text

from Configs import translations
from Settings import settings
from Tables import User
from src.Services import MessagesService


@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.get-message')), )
async def write_to_dev_message(message: types.Message, user: User):
    random_message = await MessagesService.get_random_message(user.id)

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
