import calendar
from datetime import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


# setting callback_data prefix and parts
class DCCallback(CallbackData, prefix="dialog_calendar"):
    act: str
    year: int
    month: int
    day: int

ignore_callback = DCCallback(act="IGNORE", year=-1, month=-1, day=-1).pack()  # for buttons with no answer


class DialogCalendar:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self, year: int = datetime.now().year, month: int = datetime.now().month):
        self.year = year
        self.month = month

    async def start_calendar(self, year: int = datetime.now().year) -> InlineKeyboardMarkup:

        # years
        first_row = [
            InlineKeyboardButton(text=str(value), callback_data=DCCallback(act="SET-YEAR", year=value, month=-1, day=-1).pack())
            for value in range(year - 2, year + 3)
        ]

        # nav buttons
        naw_row = [
            InlineKeyboardButton(text='<<', callback_data=DCCallback(act="PREV-YEARS", year=year, month=-1, day=-1).pack()),
            InlineKeyboardButton(text='>>', callback_data=DCCallback(act="NEXT-YEARS", year=year, month=-1, day=-1).pack())
        ]

        return InlineKeyboardMarkup(inline_keyboard=[first_row, naw_row])

    async def _get_month_kb(self, year: int):
        
        # first row with year button
        first_row = [
            InlineKeyboardButton(text=" ", callback_data=ignore_callback),
            InlineKeyboardButton(text=str(year),
                                callback_data=DCCallback(act="START", year=year, month=-1, day=-1).pack()),
            InlineKeyboardButton(text=" ", callback_data=ignore_callback)
        ]

        # two rows with 6 months buttons
        month_rows = [
            [InlineKeyboardButton(text=month, callback_data=DCCallback(act="SET-MONTH", year=year, month=self.months.index(month) + 1, day=-1).pack())
            for month in self.months[0:6]],
            [InlineKeyboardButton(text=month, callback_data=DCCallback(act="SET-MONTH", year=year, month=self.months.index(month) + 1, day=-1).pack())
            for month in self.months[6:12]]
        ]
        
        return InlineKeyboardMarkup(inline_keyboard=[first_row, *month_rows])

    async def _get_days_kb(self, year: int, month: int):
        
        month_calendar = calendar.monthcalendar(year, month)

        inline_kb = [
            [InlineKeyboardButton(text=str(year), callback_data=DCCallback(act="START", year=year, month=-1, day=-1).pack()),
            InlineKeyboardButton(text=self.months[month - 1], callback_data=DCCallback(act="SET-YEAR", year=year, month=-1, day=-1).pack())],
            [InlineKeyboardButton(text=day, callback_data=ignore_callback)
                for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]],
        ]

        weeks_row = []
        for week in month_calendar:
            _week = []
            for day in week:
                if (day == 0):
                    _week.append(InlineKeyboardButton(text=" ", callback_data=ignore_callback))
                    continue
                _week.append(
                    InlineKeyboardButton(text=str(day),
                                        callback_data=DCCallback(act="SET-DAY", year=year, month=month, day=day).pack()))
            weeks_row.append(_week)

        inline_kb.extend(weeks_row)

        return InlineKeyboardMarkup(inline_keyboard=inline_kb)

    async def process_selection(self, query: CallbackQuery, data: CallbackData) -> tuple:
        return_data = (False, None)
        if data.act == "IGNORE":
            await query.answer(cache_time=60)
        if data.act == "SET-YEAR":
            await query.message.edit_reply_markup(reply_markup = await self._get_month_kb(int(data.year)))
        if data.act == "PREV-YEARS":
            new_year = int(data.year) - 5
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(new_year))
        if data.act == "NEXT-YEARS":
            new_year = int(data.year) + 5
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(new_year))
        if data.act == "START":
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(int(data.year)))
        if data.act == "SET-MONTH":
            await query.message.edit_reply_markup(reply_markup = await self._get_days_kb(int(data.year), int(data.month)))
        if data.act == "SET-DAY":
            await query.message.delete_reply_markup()   # removing inline keyboard
            return_data = True, datetime(int(data.year), int(data.month), int(data.day))
        return return_data
