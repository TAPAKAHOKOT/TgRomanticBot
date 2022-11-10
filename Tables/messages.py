from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    BigInteger,
    DateTime,
    text
)
from sqlalchemy.orm import (
    Session
)

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel


class Messages(Base, BaseModel):
    __tablename__ = 'messages'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    added_by = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    chat_id = Column(BigInteger, nullable=False)
    message_id = Column(BigInteger, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return Messages

    @staticmethod
    def get_all(session: Session) -> list:
        return session.query(Messages).all()

    @staticmethod
    def find_by_id(session: Session, id: int) -> 'Messages':
        return session.query(Messages).where(
            Messages.id == id
        ).first()

    @staticmethod
    def get_all_except(session: Session, id_list: list) -> list:
        return session.query(Messages).filter(
            Messages.id.not_in(id_list)
        ).all()

    @staticmethod
    def delete(session: Session, id: int):
        return session.query(Messages).where(
            Messages.id == id
        ).delete()


messages_table = Messages.__table__
