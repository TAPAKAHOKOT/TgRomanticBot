from random import choice

from sqlalchemy.orm import Session

from Database import engine
from Tables import (
    Messages,
    UsersGainedMessages
)
from loguru import logger


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
    async def get_random_message(user_id: int) -> dict | None:
        with Session(engine) as session, session.begin():
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
            logger.debug(list(
                    map(
                        lambda m: m.message_id,
                        except_messages
                    )
                ))
            logger.debug(except_messages)
            logger.debug(messages)
            logger.debug(user_id)

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

            logger.debug(random_message)

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
    async def delete_message(message_id: int):
        with Session(engine) as session, session.begin():
            Messages.delete(session, message_id)
