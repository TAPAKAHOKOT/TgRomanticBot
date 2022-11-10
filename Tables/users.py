from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    BigInteger,
    DateTime,
    text,
    or_
)
from sqlalchemy.orm import (
    relationship,
    Session
)

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel
from Tables.roles import Role


class User(Base, BaseModel):
    __tablename__ = 'users'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(ForeignKey('roles.id', ondelete="SET NULL"), nullable=True)

    chat_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(String(256), nullable=True, unique=True)

    last_activity_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    role = relationship(
        'Role',
        lazy='joined'
    )

    user_settings = relationship(
        'UserSettings',
        lazy='joined',
        uselist=False,
        backref='user_settings'
    )

    def get_class(self):
        return User

    @staticmethod
    def find_by_chat_id(session: Session, chat_id: int) -> 'User':
        return session.query(User).where(
            User.chat_id == chat_id
        ).first()

    @staticmethod
    def get_all_admins(session: Session) -> list:
        return session.query(User).join(Role).where(
            or_(Role.role == 'root', Role.role == 'admin')
        ).all()

    @staticmethod
    def get_all_users(session: Session) -> list:
        return session.query(User).all()


users_table = User.__table__
