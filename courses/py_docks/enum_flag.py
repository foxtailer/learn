from enum import Flag
from datetime import date

 
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())


def show_chores(chores, day):
    day = Weekday.from_date(day)

    for chore, days in chores.items():
        if day in days:
            print(chore)


chores_for_ethan = {
'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
'answer SO questions': Weekday.SATURDAY,
}


show_chores(chores_for_ethan, date.today())