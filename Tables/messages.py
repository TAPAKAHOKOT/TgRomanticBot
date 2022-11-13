from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    BigInteger,
    DateTime,
    String,
    and_,
    text
)
from sqlalchemy.orm import (
    Session
)

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel
from src.Enums import MessagesStatusEnum


class Messages(Base, BaseModel):
    __tablename__ = 'messages'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    added_by = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    chat_id = Column(BigInteger, nullable=False)
    message_id = Column(BigInteger, nullable=False)
    status = Column(String, nullable=False, default=MessagesStatusEnum.ACTIVE, server_default=MessagesStatusEnum.ACTIVE)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return Messages

    @staticmethod
    def get_all_with_trash(session: Session) -> list:
        return session.query(Messages).order_by(Messages.id).all()

    @staticmethod
    def get_all(session: Session) -> list:
        return session.query(Messages).where(
            Messages.status == MessagesStatusEnum.ACTIVE
        ).order_by(Messages.id).all()

    @staticmethod
    def find_by_id(session: Session, id: int) -> 'Messages':
        return session.query(Messages).where(
            and_(Messages.id == id, Messages.status == MessagesStatusEnum.ACTIVE)
        ).first()

    @staticmethod
    def find_by_id_with_trash(session: Session, id: int) -> 'Messages':
        return session.query(Messages).where(
            Messages.id == id
        ).first()

    @staticmethod
    def get_all_except(session: Session, id_list: list) -> list:
        return session.query(Messages).where(
            Messages.status == MessagesStatusEnum.ACTIVE
        ).filter(
            Messages.id.not_in(id_list)
        ).all()

    @staticmethod
    def delete(session: Session, id: int):
        return session.query(Messages).where(
            Messages.id == id
        ).update({'status': MessagesStatusEnum.DELETED})

    @staticmethod
    def restore(session: Session, id: int):
        return session.query(Messages).where(
            Messages.id == id
        ).update({'status': MessagesStatusEnum.ACTIVE})


messages_table = Messages.__table__
