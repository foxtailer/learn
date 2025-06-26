from aiogram.filters import BaseFilter
from aiogram.types import Message


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message) -> bool:
        return (obj.from_user.id in [1, 2]) == self.is_admin
