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


class UsersGainedMessages(Base, BaseModel):
    __tablename__ = 'users_gained_messages'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    message_id = Column(BigInteger, ForeignKey('messages.id', ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return UsersGainedMessages

    @staticmethod
    def find_by_user_id(session: Session, user_id: int) -> list:
        return session.query(UsersGainedMessages).where(
            UsersGainedMessages.user_id == user_id
        ).all()

    @staticmethod
    def get_count_for_today(session: Session, user_id: int) -> int:
        return session.query(UsersGainedMessages).where(
            UsersGainedMessages.user_id == user_id
        ).filter(
            extract('month', UsersGainedMessages.created_at) == datetime.today().month,
            extract('year', UsersGainedMessages.created_at) == datetime.today().year,
            extract('day', UsersGainedMessages.created_at) == datetime.today().day
        ).count()

    @staticmethod
    def get_last_by_user_id(session: Session, user_id: int) -> 'UsersGainedMessages':
        return session.query(UsersGainedMessages).where(
            UsersGainedMessages.user_id == user_id
        ).order_by(desc(UsersGainedMessages.created_at)).first()

    @staticmethod
    def get_all_in(session: Session, user_id: int, id_list: list) -> list:
        return session.query(UsersGainedMessages).where(
            UsersGainedMessages.user_id == user_id
        ).filter(
            UsersGainedMessages.message_id.in_(id_list)
        ).all()


user_gained_messages_table = UsersGainedMessages.__table__
