from os import getenv

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.orm import Session

from Database import engine
from Tables import (
    Role,
    User
)


class SetupRoleMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        admins = map(int, getenv("ADMINS").split(','))
        chat_id = message.from_user['id']
        role: Role = data['role']

        if chat_id not in admins:
            return

        if role:
            if role.role == 'root':
                return

        with Session(engine, expire_on_commit=False) as session, session.begin():
            user: User = data['user']
            role: Role = Role.find_by_role(session, 'root')

            if user and role:
                user.role_id = role.id
                session.add(user)

                data['role'] = user.role

    async def on_process_callback_query(self, message: Message, data: dict):
        await self.on_pre_process_message(message, data)
