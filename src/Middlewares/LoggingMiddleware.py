from datetime import datetime

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from loguru import logger


class LoggingMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        logger.info(f'Message: {message}\ttime: {datetime.now()}')

    async def on_process_callback_query(self, message: Message, data: dict):
        await self.on_pre_process_message(message, data)
