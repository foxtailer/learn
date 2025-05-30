import calendar
from datetime import datetime, timedelta

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


class SCCallback(CallbackData, prefix="simple_calendar"):
    act: str
    year: int
    month: int
    day: int


class SimpleCalendar:

    async def start_calendar(self,
                             year: int = datetime.now().year,
                             month: int = datetime.now().month) -> InlineKeyboardMarkup:
        """
        Creates an inline keyboard with the provided year and month
        :param int year: Year to use in the calendar, if None the current year is used.
        :param int month: Month to use in the calendar, if None the current month is used.
        :return: Returns InlineKeyboardMarkup object with the calendar.
        """
        
        ignore_callback = SCCallback(act="IGNORE", year=year, month=month, day=0).pack()  # for buttons with no answer

        # Month and Year
        first_row = [
            InlineKeyboardButton(text="<<",
                                callback_data=SCCallback(act="PREV-YEAR", year=year, month=month, day=1).pack()),
            InlineKeyboardButton(text=f'{calendar.month_name[month]} {str(year)}',
                                callback_data=ignore_callback),
            InlineKeyboardButton(text=">>",
                                callback_data=SCCallback(act="NEXT-YEAR", year=year, month=month, day=1).pack())
        ]

        # Week Days
        second_row = [
            InlineKeyboardButton(text=day, callback_data=ignore_callback)
            for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        ]

        # Days of month
        calendar_rows = []
        month_calendar = calendar.monthcalendar(year, month)

        for week in month_calendar:
            week_row =[]

            for day in week:
                if (day == 0):
                    week_row.append(InlineKeyboardButton(text=" ", callback_data=ignore_callback))
                    continue
                week_row.append(InlineKeyboardButton(text=str(day),
                                     callback_data=SCCallback(act="DAY", year=year, month=month, day=day).pack()))
            calendar_rows.append(week_row)

        # Buttons
        last_row = [
            InlineKeyboardButton(text="<",
                                callback_data=SCCallback(act="PREV-MONTH", year=year, month=month, day=day).pack()),
            InlineKeyboardButton(text=" ", callback_data=ignore_callback),
            InlineKeyboardButton(text=">", callback_data=SCCallback(act="NEXT-MONTH", year=year, month=month, day=day).pack())
        ]

        inline_kb = [first_row, second_row, *calendar_rows, last_row]

        return InlineKeyboardMarkup(inline_keyboard=inline_kb)

    async def process_selection(self, query: CallbackQuery, data: CallbackData) -> tuple:
        """
        Process the callback_query. This method generates a new calendar if forward or
        backward is pressed. This method should be called inside a CallbackQueryHandler.
        :param query: callback_query, as provided by the CallbackQueryHandler
        :param data: callback_data, dictionary, set by calendar_callback
        :return: Returns a tuple (Boolean,datetime), indicating if a date is selected
                    and returning the date if so.
        """

        return_data = (False, None)
        temp_date = datetime(int(data.year), int(data.month), 1)
        # processing empty buttons, answering with no action
        if data.act == "IGNORE":
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if data.act == "DAY":
            await query.message.delete_reply_markup()   # removing inline keyboard
            return_data = True, datetime(int(data.year), int(data.month), int(data.day))
        # user navigates to previous year, editing message with new calendar
        if data.act == "PREV-YEAR":
            prev_date = datetime(int(data.year) - 1, int(data.month), 1)
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next year, editing message with new calendar
        if data.act == "NEXT-YEAR":
            next_date = datetime(int(data.year) + 1, int(data.month), 1)
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(int(next_date.year), int(next_date.month)))
        # user navigates to previous month, editing message with new calendar
        if data.act == "PREV-MONTH":
            prev_date = temp_date - timedelta(days=1)
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next month, editing message with new calendar
        if data.act == "NEXT-MONTH":
            next_date = temp_date + timedelta(days=31)
            await query.message.edit_reply_markup(reply_markup = await self.start_calendar(int(next_date.year), int(next_date.month)))
        # at some point user clicks DAY button, returning date
        return return_data
