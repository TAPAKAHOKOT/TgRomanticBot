import sys
from configparser import ConfigParser

from .Translations import Translations

app_config = ConfigParser()
app_config.read(sys.path[0] + "/Configs/app.ini")


def get_available_languages():
    languages = app_config.get('DEFAULT', 'available-languages').split(',')
    return map(lambda l: l.title(), languages)


def get_default_language() -> str:
    return app_config.get('DEFAULT', 'language')


translations = Translations(
    get_default_language()
)
