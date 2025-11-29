from aiogram.filters import BaseFilter


class FirstCharFilter(BaseFilter):
    def __init__(self, char: str):
        self.char = char

    async def __call__(self, message) -> bool:
        return message.text.startswith(self.char)