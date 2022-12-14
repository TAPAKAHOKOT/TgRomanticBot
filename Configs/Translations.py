from loguru import logger

from Settings import settings
from .languages.russian import translations as russian


class Translations:
    def __init__(self):
        self.default_language = 'russian'
        self.all_translations = {
            'russian': russian
        }
        self.current_language = None

    def set_translation(self, user_language: str):
        if user_language in self.all_translations.keys():
            self.current_language = user_language

    def get_translation(self):
        try:
            if self.current_language:
                return self.all_translations[self.current_language]
            return self.all_translations[self.default_language]
        except KeyError:
            logger.error(f'key {self.default_language} not found in Translations.all_translations')
            return None

    def get_recoursive(self, keys: list, translations: dict, default: any = '') -> str:
        if keys[0] in translations.keys():
            if (len(keys) == 1):
                return translations[keys[0]]
            return self.get_recoursive(keys[1:], translations[keys[0]], default)
        return default

    def get(self, key: str, default: any = ''):
        custom_translation = self.get_recoursive(
            key.split('.'),
            settings.custom_translations
        )
        if custom_translation:
            return custom_translation

        return self.get_recoursive(
            key.split('.'),
            self.get_translation()
        )

    def get_in_all_languages(self, key: str) -> list:
        values = []
        keys = key.split('.')
        for translations in self.all_translations.values():
            custom_translation = self.get_recoursive(
                key.split('.'),
                settings.custom_translations
            )
            if custom_translation:
                values.append(custom_translation)
                continue

            value = self.get_recoursive(
                keys,
                translations
            )
            if value:
                values.append(value)
        return values
