from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils.exceptions import BadRequest
from loguru import logger

from Settings import settings
from Tables import User
from src.Callbacks import AnswerCallback
from src.Filters.RolesFilter import IsRootFilter
from src.Services import MessagesService
from src.States import AnswerForm


@settings.dp.message_handler(IsRootFilter(), commands=['load_env'])
async def get_all_messages(message: types.Message):
    settings.load_env()
    await message.answer('Настройки обновлены')


@settings.dp.message_handler(IsRootFilter(), commands=['load_custom_translations'])
async def get_all_messages(message: types.Message):
    settings.load_custom_translations()
    await message.answer('Переводы обновлены')


@settings.dp.message_handler(IsRootFilter(), commands=['get_all_messages'])
async def get_all_messages(message: types.Message):
    all_messages = await MessagesService.get_all_messages()
    await message.answer(f'Все загруженные сообщения:\n\n--------------------\n{all_messages}\n--------------------')


@settings.dp.message_handler(IsRootFilter(), commands=['get_all_messages_with_trash'])
async def get_all_messages(message: types.Message):
    all_messages = await MessagesService.get_all_messages_with_trash()
    await message.answer(
        f'Все загруженные и удаленные сообщения:\n\n--------------------\n{all_messages}\n--------------------')


@settings.dp.message_handler(IsRootFilter(), commands=['get_unread_messages'])
async def get_unread_messages(message: types.Message):
    chat_id = message.text.replace('/get_unread_messages', '').replace(' ', '')

    if not chat_id.isdigit():
        if not settings.enabled_users or len(settings.enabled_users) > 1:
            await message.answer('Форма записи команды /get_unread_messages:\n/left_messages_count <ID пользователя>')
            return
        else:
            chat_id = settings.enabled_users[0]

    username, messages_left_count, unread_messages = await MessagesService.get_left_messages_count(int(chat_id))
    horizontal, vertical = await MessagesService.format_id_list(unread_messages)

    await message.answer(
        f'У пользователя [ <a href=\'https://t.me/{username}\'>{username}</a> ] ' +
        f'[<a href=\'https://web.telegram.org/k/#{chat_id}\'>{chat_id}</a>] ' +
        f'осталось <b>{messages_left_count}</b> непрочитанных сообщений:\n{vertical}',
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
    await message.answer(f'/get {horizontal}')


@settings.dp.message_handler(IsRootFilter(), commands=['delete'])
async def delete_message(message: types.Message):
    message_id_str = message.text.replace('/delete ', '')

    is_iterated = False
    if '-' in message_id_str:
        message_id_str_split = message_id_str.replace(' ', '').split('-')
        if len(message_id_str_split) == 2:
            for message_id in range(int(message_id_str_split[0]), int(message_id_str_split[1]) + 1):
                is_iterated = True
                try:
                    if await MessagesService.is_message_exists(int(message_id)):
                        await MessagesService.delete_message(int(message_id))
                        await message.answer(f'Сообщение {message_id} удалено')
                except Exception as e:
                    logger.error(e)
                    continue

    for message_id in message_id_str.replace(' ', '').split(','):
        if message_id.isdigit():
            is_iterated = True
            try:
                await MessagesService.delete_message(int(message_id))
                await message.answer(f'Сообщение {message_id} удалено')
            except Exception as e:
                logger.error(e)
                continue
    if not is_iterated:
        await message.answer('Форма записи команды /delete:\n/delete <число>, <число>, ...\n/delete <число>-<число>')


@settings.dp.message_handler(IsRootFilter(), commands=['restore'])
async def restore_message(message: types.Message):
    message_id_str = message.text.replace('/restore ', '')

    is_iterated = False
    if '-' in message_id_str:
        message_id_str_split = message_id_str.replace(' ', '').split('-')
        if len(message_id_str_split) == 2:
            for message_id in range(int(message_id_str_split[0]), int(message_id_str_split[1]) + 1):
                is_iterated = True
                try:
                    if await MessagesService.is_message_exists(int(message_id)):
                        await MessagesService.restore_message(int(message_id))
                        await message.answer(f'Сообщение {message_id} восстановлено')
                except Exception as e:
                    logger.error(e)
                    continue

    for message_id in message_id_str.replace(' ', '').split(','):
        if message_id.isdigit():
            is_iterated = True
            try:
                await MessagesService.restore_message(int(message_id))
                await message.answer(f'Сообщение {message_id} восстановлено')
            except Exception as e:
                logger.error(e)
                continue
    if not is_iterated:
        await message.answer('Форма записи команды /restore:\n/restore <число>, <число>, ...\n/restore <число>-<число>')


@settings.dp.message_handler(IsRootFilter(), commands=['get', 'get_with_trash'])
async def get_message(message: types.Message):
    with_trash = 'get_with_trash' in message.text
    message_id_str = message.text.replace('/get_with_trash ' if with_trash else '/get ', '')

    is_iterated = False
    if '-' in message_id_str:
        message_id_str_split = message_id_str.replace(' ', '').split('-')
        if len(message_id_str_split) == 2:
            for message_id in range(int(message_id_str_split[0]), int(message_id_str_split[1]) + 1):
                is_iterated = True
                try:
                    message_data = await MessagesService.get_message_with_trash(int(message_id)) if with_trash else \
                        await MessagesService.get_message(int(message_id))
                except Exception:
                    continue

                await message.answer(f'Сообщение {message_id}:')
                try:
                    await settings.bot.copy_message(
                        from_chat_id=message_data['chat_id'],
                        chat_id=message.chat.id,
                        message_id=message_data['message_id']
                    )
                except BadRequest:
                    await message.answer('удалено')

    for message_id in message_id_str.replace(' ', '').split(','):
        if message_id.isdigit():
            is_iterated = True
            try:
                message_data = await MessagesService.get_message_with_trash(int(message_id)) if with_trash else \
                    await MessagesService.get_message(int(message_id))
            except Exception as e:
                logger.error(e)
                continue

            await message.answer(f'Сообщение {message_id}:')
            try:
                await settings.bot.copy_message(
                    from_chat_id=message_data['chat_id'],
                    chat_id=message.chat.id,
                    message_id=message_data['message_id']
                )
            except BadRequest:
                await message.answer('удалено')

    if not is_iterated:
        await message.answer('Форма записи команды /get:\n/get <число>, <число>, ...\n/get <число>-<число>')


@settings.dp.message_handler(IsRootFilter(), commands=['left_messages_count'])
async def func(message: types.Message):
    chat_id = message.text.replace('/left_messages_count', '').replace(' ', '')

    if not chat_id.isdigit():
        if not settings.enabled_users or len(settings.enabled_users) > 1:
            await message.answer('Форма записи команды /left_messages_count:\n/left_messages_count <число>')
            return
        else:
            chat_id = settings.enabled_users[0]

    username, messages_left_count, _ = await MessagesService.get_left_messages_count(int(chat_id))

    await message.answer(
        f'У пользователя [ <a href=\'https://t.me/{username}\'>{username}</a> ] ' +
        f'[<a href=\'https://web.telegram.org/k/#{chat_id}\'>{chat_id}</a>] ' +
        f'осталось <b>{messages_left_count}</b> непрочитанных сообщений',
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


@settings.dp.callback_query_handler(
    AnswerCallback.get_answer_inline_data().filter()
)
async def write_to_dev_message(call: types.CallbackQuery):
    _, username, chat_id, reply_message_id = call.data.split(':')

    state = AnswerForm.answer
    await state.set()

    state = Dispatcher.get_current().current_state()
    await state.update_data({
        'username': username,
        'chat_id': chat_id,
        'reply_message_id': reply_message_id
    })

    await call.message.answer(
        f'Следующее твое сообщение будет скопировано пользователю [ <a href=\'https://t.me/{username}\'>{username}</a> ] [<a href=\'https://web.telegram.org/k/#{chat_id}\'>{chat_id}</a>]',
        reply_markup=AnswerCallback.get_cancel_inline(),
        parse_mode=ParseMode.HTML,
    )


@settings.dp.message_handler(
    IsRootFilter(),
    content_types=['any'],
    state=AnswerForm.answer
)
async def write_to_dev_message(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    await state.finish()

    await settings.bot.copy_message(
        from_chat_id=message.chat.id,
        chat_id=state_data.get('chat_id'),
        message_id=message.message_id,
        reply_to_message_id=state_data.get('reply_message_id')
    )
    await message.answer('Сообщение скопировано', reply=True)


@settings.dp.callback_query_handler(
    AnswerCallback.get_cancel_inline_data().filter()
)
async def write_to_dev_message(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()


@settings.dp.message_handler(
    IsRootFilter(),
    content_types=['any']
)
async def save_any_message(message: types.Message, user: User):
    if message.reply_to_message is None:
        saved_message_id = await MessagesService.add_message(
            user.id,
            message.from_user.id,
            message.message_id
        )
        await message.answer(f'Id сообщения: {saved_message_id}', reply=True)
    else:
        msg, user = await MessagesService.get_user_message_by_bot_message(message.reply_to_message.message_id)
        await settings.bot.copy_message(
            from_chat_id=message.chat.id,
            chat_id=user.chat_id,
            message_id=message.message_id,
            reply_to_message_id=msg.user_message_id
        )
