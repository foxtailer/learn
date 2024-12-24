#  How to annotations
"""
In Python, __annotations__ is a special attribute used to store type hints or annotations 
specified for variables, function arguments, or return types. It's a dictionary where the 
keys are the names of the variables or parameters, and the values are the corresponding 
type hints.
"""
class o:
    a: int = 3
    b: str = 'abc'

if isinstance(o, type):
    ann = o.__dict__.get('__annotations__', None)  # {'a': <class 'int'>, 'b': <class 'str'>}
else:
    ann = getattr(o, '__annotations__', None)

"""
“Stringized” annotations refer to the feature in Python where type hints are stored as strings 
instead of direct Python objects.
"""
from typing import List, get_type_hints

def greet(names: List[str]) -> None:
    pass

print(greet.__annotations__)  # {'names': 'List[str]', 'return': 'None'}
hints = get_type_hints(greet)  # {'names': typing.List[str], 'return': <class 'NoneType'>}


# How to enums
"""
An Enum is a set of symbolic names bound to unique values. Used to represent constants. They 
are similar to global variables , but they offer a more useful repr(), grouping, type-safety,
and a few other features.
"""
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

"""
Depending on the nature of the enum a member’s value may or may not be important, but either 
way that value can be used to get the corresponding member:
"""
Weekday(3)  # <Weekday.WEDNESDAY: 3>

"""
The type of an enumeration member is the enum it belongs to:
"""
type(Weekday.MONDAY)  # <enum 'Weekday'>
isinstance(Weekday.FRIDAY, Weekday)  # True

print(Weekday.TUESDAY.name)  # TUESDAY
Weekday.WEDNESDAY.value  # 3

"""
Python Enums can have behavior added.
"""
from enum import Enum
from datetime import date

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

print(type(date.today()))  # <class 'datetime.date'>
print(date.today().__str__())  # 2024-12-24
print(date.today().__repr__())  # datetime.date(2024, 12, 24)
print(date.today().isoweekday())  # today number 1-7

print(Weekday.from_date(date.today()))