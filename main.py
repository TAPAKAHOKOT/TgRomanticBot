from aiogram import executor
from loguru import logger

from src.Handlers import *
from src.Middlewares import (
    LoggingMiddleware,
    UserMiddleware,
    SetupRoleMiddleware,
    TranslationMiddleware
)


async def on_startup(x):
    logger.info('Bot started')


async def on_shutdown(x):
    logger.info('Bot finished')


def setup_middlewares():
    settings.dp.middleware.setup(LoggingMiddleware())
    settings.dp.middleware.setup(UserMiddleware())
    settings.dp.middleware.setup(SetupRoleMiddleware())
    settings.dp.middleware.setup(TranslationMiddleware())


# def bind_filters():
#     settings.dp.filters_factory.bind(RolesFilter)


def start_polling():
    setup_middlewares()
    executor.start_polling(settings.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    logger.info('Script finished')


if __name__ == '__main__':
    start_polling()
