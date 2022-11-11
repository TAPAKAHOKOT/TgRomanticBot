from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

logger.info('Loaded dotenv')


class Settings:
    def __init__(self):
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

        self.messages = []
