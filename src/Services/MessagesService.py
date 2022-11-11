from random import choice

from sqlalchemy.orm import Session

from Database import engine
from Tables import (
    Messages,
    UsersGainedMessages
)
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

            return '\n--------------------\n\n--------------------\n'.join(
                list(
                    map(
                        lambda m: f'id: {m.id}\nadded_by: {m.added_by}\nmessage_id: {m.message_id}',
                        all_messages
                    )
                )
            )

    @staticmethod
    async def get_random_message(user_id: int, hours_limit: int, messages_limit: int) -> dict | str | None:
        with Session(engine) as session, session.begin():
            last_except_messages = UsersGainedMessages.get_last_by_user_id(session, user_id)

            if len(last_except_messages) >= messages_limit:
                except_messages_to_count = last_except_messages[messages_limit-1]
                total_seconds_left = DateService.get_seconds_left(except_messages_to_count.created_at, hours_limit)

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
    async def is_message_exists(message_id: int):
        with Session(engine) as session, session.begin():
            return bool(Messages.find_by_id(session, message_id))

    @staticmethod
    async def delete_message(message_id: int):
        with Session(engine) as session, session.begin():
            Messages.delete(session, message_id)
