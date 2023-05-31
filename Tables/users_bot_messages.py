from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    BigInteger,
    DateTime,
    text,
    desc,
    extract
)
from sqlalchemy.orm import (
    Session
)

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel


class UsersBotMessages(Base, BaseModel):
    __tablename__ = 'users_bot_messages'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    user_message_id = Column(BigInteger, nullable=False)
    bot_message_id = Column(BigInteger, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return UsersBotMessages

    @staticmethod
    def find_by_bot_message_id(session: Session, bot_message_id: int) -> list:
        return session.query(UsersBotMessages).where(
            UsersBotMessages.bot_message_id == bot_message_id
        ).first()


users_bot_messages_table = UsersBotMessages.__table__
