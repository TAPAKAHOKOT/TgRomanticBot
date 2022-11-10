from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types import Message

from Tables import Role


class BaseRoleFilter:
    @staticmethod
    def check_role():
        user_role: Role = ctx_data.get()['role']
        return user_role.role if user_role else None


class IsRootFilter(BoundFilter):
    async def check(self, message: Message) -> bool:
        return BaseRoleFilter.check_role() == 'root'


class IsAdminFilter(BoundFilter):
    async def check(self, message: Message) -> bool:
        return BaseRoleFilter.check_role() == 'admin'
