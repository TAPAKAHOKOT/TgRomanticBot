from aiogram import types
from aiogram.dispatcher.filters import Text

from Configs import translations
from Settings import settings
from Tables import User
from src.Filters.RolesFilter import IsRootFilter
from src.Services import MessagesService


@settings.dp.message_handler(IsRootFilter(), commands=['get_all_messages'])
async def get_all_messages(message: types.Message):
    all_messages = await MessagesService.get_all_messages()
    await message.answer(f'Все сообщения:\n\n--------------------\n{all_messages}\n--------------------')


@settings.dp.message_handler(IsRootFilter(), commands=['delete'])
async def delete_message(message: types.Message):
    message_id_str = message.text.replace('/delete ', '')

    is_iterated = False
    for message_id in message_id_str.replace(' ', '').split(','):
        if message_id.isdigit():
            is_iterated = True

            try:
                await MessagesService.delete_message(int(message_id))
                await message.answer(f'Сообщение {message_id} удалено')
            except Exception:
                continue
    if not is_iterated:
        await message.answer('Форма записи команды /delete:\n/delete <число>, <число>, ...')


@settings.dp.message_handler(IsRootFilter(), commands=['get'])
async def get_message(message: types.Message):
    message_id_str = message.text.replace('/get ', '')

    is_iterated = False
    for message_id in message_id_str.replace(' ', '').split(','):
        if message_id.isdigit():
            is_iterated = True

            try:
                message_data = await MessagesService.get_message(int(message_id))
            except Exception:
                continue

            await message.answer(f'Сообщение {message_id}:')
            await settings.bot.copy_message(
                from_chat_id=message_data['chat_id'],
                chat_id=message.chat.id,
                message_id=message_data['message_id']
            )

    if not is_iterated:
        await message.answer('Форм записи команды /get:\n/get <число>, <число>, ...')


@settings.dp.message_handler(
    Text(equals=translations.get_in_all_languages('keyboards.buttons.get-message')),
    IsRootFilter(),
    content_types=['any']
)
async def save_any_message(message: types.Message, user: User):
    saved_message_id = await MessagesService.add_message(
        user.id,
        message.from_user.id,
        message.message_id
    )
    await message.answer(f'Id сообщения: {saved_message_id}', reply=True)
