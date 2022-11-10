from datetime import datetime

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.orm import Session

from Database import engine
from Tables import (
    User,
    UserSettings
)


class UserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        chat_id = message.from_user['id']
        username = message.from_user['username']

        with Session(engine) as session, session.begin():
            user: User = User.find_by_chat_id(session, chat_id)
            if not user:
                user = User(
                    chat_id=chat_id,
                    username=username
                )
            user.last_activity_at = datetime.now()
            session.add(user)

        with Session(engine, expire_on_commit=False) as session, session.begin():
            user: User = User.find_by_chat_id(session, chat_id)
            user_settings: UserSettings = user.user_settings
            if not user_settings:
                user_settings = UserSettings(
                    user_id=user.id
                )
            session.add(user_settings)

            data['user'] = user
            data['role'] = user.role
            data['user_settings'] = user_settings

    async def on_process_callback_query(self, message: Message, data: dict):
        await self.on_pre_process_message(message, data)
