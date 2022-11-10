from loguru import logger

from .languages.english import translations as english
from .languages.russian import translations as russian


class Translations:
    def __init__(self, default_language: str):
        self.default_language = default_language
        self.all_translations = {
            'english': english,
            'russian': russian
        }
        self.current_language = None

    def set_translation(self, user_language: str) -> str:
        if user_language in self.all_translations.keys():
            self.current_language = user_language

    def get_translation(self):
        try:
            if self.current_language:
                return self.all_translations[self.current_language]
            return self.all_translations[self.default_language]
        except KeyError:
            logger.error(f'key {self.default_language} not found in Translations.all_translations')
            raise KeyError

    def get_recoursive(self, keys: list, translations: dict, default: any = '') -> str:
        if keys[0] in translations.keys():
            if (len(keys) == 1):
                return translations[keys[0]]
            return self.get_recoursive(keys[1:], translations[keys[0]], default)
        return default

    def get(self, key: str, default: any = ''):
        return self.get_recoursive(
            key.split('.'),
            self.get_translation()
        )

    def get_in_all_languages(self, key: str) -> list:
        values = []
        keys = key.split('.')
        for translations in self.all_translations.values():
            value = self.get_recoursive(
                keys,
                translations
            )
            if value: values.append(value)
        return values
