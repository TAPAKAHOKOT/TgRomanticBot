from .DefaultEnum import DefaultEnum


class MessagesStatusEnum(str, DefaultEnum):
    ACTIVE = 'active'
    DELETED = 'deleted'
