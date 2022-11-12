from sqlalchemy.orm import Session

from Database import engine
from Tables import BotSettings as BotSettingsDB


class BotSettings:
    def __init__(self):
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        self.settings = {}
        with Session(engine) as session, session.begin():
            bot_settings_list: list[BotSettingsDB] = BotSettingsDB.get_all(session)

            for bot_setting in bot_settings_list:
                self.settings[bot_setting.name] = {
                    'value': bot_setting.value,
                    'created_at': bot_setting.created_at
                }

    def set(self, name, value):
        with Session(engine) as session, session.begin():
            new_bot_settings = BotSettingsDB(
                name=name,
                value=value
            )
            session.add(new_bot_settings)
            session.flush()
            session.refresh(new_bot_settings)

            self.load_settings()

    def update(self, name, value):
        with Session(engine) as session, session.begin():
            new_bot_settings = BotSettingsDB.get_by_name(session, name)
            new_bot_settings.value = value

            session.add(new_bot_settings)
            session.flush()
            session.refresh(new_bot_settings)

            self.load_settings()

    def get(self, key):
        if key not in self.settings.keys():
            return None
        return self.settings[key]


bot_settings = BotSettings()
