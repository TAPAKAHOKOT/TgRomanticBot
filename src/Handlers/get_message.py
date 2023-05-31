from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode

from Configs import translations
from Settings import settings
from Tables import User
from src.Services import MessagesService
from src.Callbacks import AnswerCallback
from loguru import logger


@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.get-message')))
async def write_to_dev_message(message: types.Message, user: User):
    random_message = await MessagesService.get_random_message(
        user.id,
        settings.limits['hours'],
        settings.limits['messages'],
        settings.limits['random_from'],
        settings.limits['random_till']
    )

    if random_message is None:
        await message.answer('Нет доступных сообщений')
        return

    if isinstance(random_message, str):
        await message.answer(
            translations.get('answers.try-later').format(
                random_message=random_message
            )
        )
        return

    new_message = await settings.bot.copy_message(
        from_chat_id=random_message['chat_id'],
        chat_id=message.chat.id,
        message_id=random_message['message_id']
    )

    try:
        if settings.resend_to:
            for chat_id in settings.resend_to:
                await settings.bot.send_message(
                    chat_id=chat_id,
                    text=f'<a href=\'https://t.me/{user.username}\'>{user.username}</a> получил сообщение:',
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True
                )
                msg = await settings.bot.copy_message(
                    from_chat_id=random_message['chat_id'],
                    chat_id=chat_id,
                    message_id=random_message['message_id']
                )

                await MessagesService.save_sent_message(user.id, new_message.message_id, msg.message_id)
    except Exception as e:
        logger.error(e)
