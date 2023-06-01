from aiogram import types
from aiogram.types import ParseMode

from Settings import settings
from Tables import User
from src.Services import MessagesService
from loguru import logger


@settings.dp.message_handler(content_types=['any'])
async def save_any_message(message: types.Message, user: User):
    try:
        if settings.resend_to:
            for chat_id in settings.resend_to:
                if not settings.enabled_users or len(settings.enabled_users) > 1:
                    await settings.bot.send_message(
                        chat_id=chat_id,
                        text=f'Сообщение от <a href=\'https://t.me/{user.username}\'>{user.username}</a>:',
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=True
                    )
                msg = await settings.bot.copy_message(
                    from_chat_id=message.chat.id,
                    chat_id=chat_id,
                    message_id=message.message_id
                )

                await MessagesService.save_sent_message(user.id, message.message_id, msg.message_id)

    except Exception as e:
        logger.error(e)
