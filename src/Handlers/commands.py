from aiogram import types

from Configs import translations
from Settings import settings
from src.Filters import IsRootFilter, IsAdminFilter
from src.Keyboards import CommandsKeyboards


@settings.dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'],
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=CommandsKeyboards.get_main_keyboard()
    )


@settings.dp.message_handler(IsRootFilter(), commands=["help"])
async def command_help(message: types.Message):
    await message.answer(translations.get('commands.answers.help'))


@settings.dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer(translations.get('commands.answers.help-all'))


@settings.dp.message_handler(IsRootFilter(), commands=["role"])
async def command_role(message: types.Message):
    await message.answer(translations.get('commands.answers.role.root'))


@settings.dp.message_handler(IsAdminFilter(), commands=["role"])
async def command_role(message: types.Message):
    await message.answer(translations.get('commands.answers.role.admin'))


@settings.dp.message_handler(commands=["role"])
async def command_role(message: types.Message):
    await message.answer(translations.get('commands.answers.role.user'))
