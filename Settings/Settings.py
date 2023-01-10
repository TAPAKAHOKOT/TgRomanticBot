import json
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

logger.info('Loaded dotenv')


class Settings:
    def __init__(self):
        self.admins = None
        self.token = None
        self.is_testing = None
        self.resend_to = None
        self.bot = None
        self.dp = None
        self.limits = None
        self.timezone = None
        self.enabled_users = None
        self.custom_translations = None

        self.load_env()
        self.load_custom_translations()

        logger.info(self)

    def __str__(self):
        attrs = vars(self)
        return '\n' + '\n'.join("\t[ %s => %s ]" % item for item in attrs.items())

    def load_env(self):
        self.is_testing = getenv('TESTING_MODE') == 'TRUE'
        logger.info(f'Is testing = {self.is_testing}')

        self.token = getenv('TEST_BOT_TOKEN') if self.is_testing else getenv('BOT_TOKEN')
        self.admins = getenv('ADMINS').split(',')

        logger.info(f'Admins = {self.admins}')

        self.resend_to = getenv('RESEND_TO').split(',')
        logger.info(f'RESEND_TO = {self.resend_to}')

        logger.info('Loaded .env variables')

        self.bot = Bot(token=self.token)
        logger.info('Created Bot')

        self.dp = Dispatcher(self.bot, storage=MemoryStorage())
        logger.info('Created Dispatcher')

        self.limits = {
            'hours': int(getenv('LIMITS_HOURS')),
            'messages': int(getenv('LIMITS_MESSAGES')),
            'random_from': int(getenv('LIMITS_RANDOM_FROM')),
            'random_till': int(getenv('LIMITS_RANDOM_TILL'))
        }
        self.timezone = getenv('TIMEZONE')

        enabled_users = getenv('ENABLED_USERS')
        if enabled_users:
            self.enabled_users = enabled_users.split(',')

    def load_custom_translations(self):
        with open('custom_translations.json') as file:
            self.custom_translations = json.load(file)
