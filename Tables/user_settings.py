from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
    text
)

from Configs import get_default_language
from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel


class UserSettings(Base, BaseModel):
    __tablename__ = 'user_settings'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"), nullable=True)

    language = Column(String(256), nullable=True, default=get_default_language())

    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return UserSettings


user_settings_table = UserSettings.__table__
