import datetime
from random import choice, randint

from sqlalchemy.orm import Session

from Configs import bot_settings
from Database import engine
from Tables import (
    Messages,
    UsersGainedMessages,
    User,
    UsersBotMessages
)
from src.Enums import MessagesStatusEnum
from .DateService import DateService


class MessagesService:
    @staticmethod
    async def add_message(added_by: int, chat_id: int, message_id: int) -> int:
        with Session(engine) as session, session.begin():
            message = Messages(
                added_by=added_by,
                chat_id=chat_id,
                message_id=message_id
            )

            session.add(message)
            session.flush()
            session.refresh(message)

            return message.id

    @staticmethod
    async def get_all_messages() -> str:
        with Session(engine) as session, session.begin():
            all_messages = Messages.get_all(session)

            return '\n'.join(
                list(
                    map(
                        lambda m: f'id: {m.id}',
                        all_messages
                    )
                )
            )

    @staticmethod
    async def get_all_messages_with_trash() -> str:
        with Session(engine) as session, session.begin():
            all_messages = Messages.get_all_with_trash(session)

            return '\n'.join(
                list(
                    map(
                        lambda m: f'id: {m.id} {"✅" if m.status == MessagesStatusEnum.ACTIVE else "❌"}',
                        all_messages
                    )
                )
            )

    @staticmethod
    async def get_random_message(
            user_id: int,
            hours_limit: int,
            default_messages_limit: int,
            random_from: int,
            random_till: int,
    ) -> dict | str | None:
        with Session(engine) as session, session.begin():
            messages_per_day_limit = bot_settings.get('messages_per_day_limit')
            if not messages_per_day_limit:
                bot_settings.set('messages_per_day_limit', default_messages_limit)
            elif messages_per_day_limit['created_at'].date() != datetime.datetime.today().date():
                bot_settings.update('messages_per_day_limit', randint(random_from, random_till))
            messages_per_day_limit = bot_settings.get('messages_per_day_limit')

            today_count = UsersGainedMessages.get_count_for_today(session, user_id)
            last_except_message = UsersGainedMessages.get_last_by_user_id(session, user_id)

            if today_count > messages_per_day_limit['value']:
                total_seconds_left = DateService.get_seconds_until_end_of_day()

                if total_seconds_left > 0:
                    return DateService.seconds_to_str(total_seconds_left)

            if today_count <= messages_per_day_limit['value'] and last_except_message:
                total_seconds_left = DateService.get_seconds_left(last_except_message.created_at, hours_limit)

                if total_seconds_left > 0:
                    return DateService.seconds_to_str(total_seconds_left)

            except_messages = UsersGainedMessages.find_by_user_id(session, user_id)
            messages = Messages.get_all_except(
                session,
                list(
                    map(
                        lambda m: m.message_id,
                        except_messages
                    )
                )
            )

            if not messages:
                return None

            random_message = choice(
                list(
                    map(
                        lambda m: {'id': m.id, 'chat_id': m.chat_id, 'message_id': m.message_id},
                        messages
                    )
                )
            )

            gained_message = UsersGainedMessages(
                user_id=user_id,
                message_id=random_message['id']
            )
            session.add(gained_message)
            session.flush()
            session.refresh(gained_message)

            return random_message

    @staticmethod
    async def get_message(message_id) -> dict:
        with Session(engine) as session, session.begin():
            message: Messages = Messages.find_by_id(session, message_id)
            return {
                'chat_id': message.chat_id,
                'message_id': message.message_id
            }

    @staticmethod
    async def get_message_with_trash(message_id) -> dict:
        with Session(engine) as session, session.begin():
            message: Messages = Messages.find_by_id_with_trash(session, message_id)
            return {
                'chat_id': message.chat_id,
                'message_id': message.message_id
            }

    @staticmethod
    async def is_message_exists(message_id: int):
        with Session(engine) as session, session.begin():
            return bool(Messages.find_by_id(session, message_id))

    @staticmethod
    async def delete_message(message_id: int):
        with Session(engine) as session, session.begin():
            Messages.delete(session, message_id)

    @staticmethod
    async def restore_message(message_id: int):
        with Session(engine) as session, session.begin():
            Messages.restore(session, message_id)

    @staticmethod
    async def get_left_messages_count(chat_id: int):
        with Session(engine) as session, session.begin():
            user = User.find_by_chat_id(session, chat_id)
            all_messages = list(map(lambda m: m.id, Messages.get_all(session)))
            gained_messages = list(map(lambda m: m.message_id, UsersGainedMessages.get_all_in(
                session,
                user.id,
                all_messages
            )))

            unread_messages = await MessagesService.get_unread_messages(
                all_messages,
                gained_messages
            )

            return user.username, len(all_messages) - len(gained_messages), unread_messages

    @staticmethod
    async def get_unread_messages(all_messages: list[int], gained_messages: list[int]) -> list[int]:
        messages = []
        for message_id in all_messages:
            if message_id not in gained_messages:
                messages.append(message_id)
        return messages

    @staticmethod
    async def format_id_list(id_list: list) -> tuple:
        id_list = list(map(str, id_list))
        return ', '.join(id_list), '\n'.join(id_list)

    @staticmethod
    async def save_sent_message(user_id: int, user_message_id: int, bot_message_id: int) -> int:
        with Session(engine) as session, session.begin():
            message = UsersBotMessages(
                user_id=user_id,
                user_message_id=user_message_id,
                bot_message_id=bot_message_id
            )

            session.add(message)
            session.flush()

    @staticmethod
    async def get_user_message_by_bot_message(bot_message_id: int) -> int:
        with Session(engine, expire_on_commit=False) as session, session.begin():
            msg = UsersBotMessages.find_by_bot_message_id(session, bot_message_id)
            user = User.find_by_id(session, msg.user_id)

            return msg, user
