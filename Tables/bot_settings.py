from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    JSON,
    Integer,
    DateTime,
    text
)
from sqlalchemy.orm import (
    Session
)

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel


class BotSettings(Base, BaseModel):
    __tablename__ = 'bot_settings'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(32), nullable=False, unique=True)
    value = Column(JSON(), nullable=False)

    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    def get_class(self):
        return BotSettings

    def get_all(session: Session) -> list:
        return session.query(BotSettings).all()

    def get_by_name(session: Session, name: str) -> 'BotSettings':
        return session.query(BotSettings).where(BotSettings.name == name).first()


bot_settings_table = BotSettings.__table__
