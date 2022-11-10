from aiogram.types import ParseMode
from sqlalchemy.orm import Session

from Configs import translations
from Database import engine
from Settings import settings
from Tables import (
    User
)


class WriteToDevService:
    @staticmethod
    async def write_to_dev(username: str, message: str):
        with Session(engine, expire_on_commit=False) as session, session.begin():
            for user in User.get_all_admins(session):
                await settings.bot.send_message(
                    user.chat_id,
                    translations.get('keyboards.answers.message-from-user').format(username=username, message=message),
                    parse_mode=ParseMode.HTML
                )
