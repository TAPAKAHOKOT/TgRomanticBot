from sqlalchemy.orm import Session

from Configs import translations
from Database import engine
from Settings import settings
from Tables import (
    User
)


class WriteToAllUsersService:
    @staticmethod
    async def write_to_all_users(message: str):
        with Session(engine, expire_on_commit=False) as session, session.begin():
            for user in User.get_all_users(session):
                await settings.bot.send_message(
                    user.chat_id,
                    translations.get('keyboards.answers.message-from-admin-to-all-users').format(message=message)
                )
