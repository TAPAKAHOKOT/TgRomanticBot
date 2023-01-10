from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

from Settings import settings
from Configs import translations


class AvailableUsersMiddleware(BaseMiddleware):
    no_access_message = translations.get('answers.no-access')

    async def on_pre_process_message(self, message: Message, data: dict):
        user_id = str(message.from_user.id)
        if not await self.is_user_enable(user_id):
            await message.answer(self.no_access_message)
            raise CancelHandler()

    async def on_process_callback_query(self, message: Message, data: dict):
        user_id = str(message.from_user.id)
        if not await self.is_user_enable(user_id):
            await message.answer(self.no_access_message)
            raise CancelHandler()

    async def is_user_enable(self, user_id) -> bool:
        if user_id in settings.admins:
            return True

        if settings.enabled_users is None or user_id in settings.enabled_users:
            return True

        return False
