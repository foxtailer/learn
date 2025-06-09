'''
Всякий раз, когда у нас есть концепция, которая имеет данные, но не
идентичность, мы часто выбираем для ее представления паттерн «Объ-
ект-значение». Объект-значение — это любой объект предметной области,
который уникально идентифицируется содержащимися в нем данными;
обычно мы делаем их немутируемыми.

Одна из приятных вещей, которые дают нам dataclasses (или named­tup­
les), — это эквивалентность значений, причудливый способ сказать, что
«две позиции заказа с одинаковыми orderid, sku и qty идентичны».

объект-значениe: это любой объект, который идентифицируется только его 
данными и не имеет долговременной идентичности.

По умолчанию — Value Object
    Если не уверен — начинай с @dataclass(frozen=True) или NamedTuple. 
    Это безопаснее и проще.
Добавляй идентичность только когда она нужна
    Не усложняй модель, пока бизнес-логика не требует уникальности и изменений.
'''

import unittest
from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.currency, self.value - other.value)
    
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.currency, self.value + other.value)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.currency, int(self.value * other))
        raise TypeError("Can only multiply Money by a number")

    def __rmul__(self, other):
        return self.__mul__(other)


Line = namedtuple('Line', ['sku', 'qty'])


def test_equality():
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Name('Harry', 'Percival') != Name('Bob', 'Gregory')
    assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)


class Person:
    '''
    люди, в отличие от имен, имеют постоянную идентичность.

    Сущности, в отличие от значений, обладают эквивалентностью идентич-
    ности (identity equality), или ее тождественностью. Мы можем изменить
    их значения, и они по-прежнему остаются узнаваемо теми же самыми.
    '''
    def __init__(self, name: Name):
        self.name = name


class TestMoneyOperations(unittest.TestCase):
    def setUp(self):
        self.fiver = Money('gbp', 5)
        self.tenner = Money('gbp', 10)

    def test_can_add_money_values_for_the_same_currency(self):
        self.assertEqual(self.fiver + self.fiver, self.tenner)

    def test_can_subtract_money_values(self):
        self.assertEqual(self.tenner - self.fiver, self.fiver)

    def test_adding_different_currencies_fails(self):
        with self.assertRaises(ValueError):
            Money('usd', 10) + Money('gbp', 10)

    def test_can_multiply_money_by_a_number(self):
        self.assertEqual(self.fiver * 5, Money('gbp', 25))

    def test_multiplying_two_money_values_is_an_error(self):
        with self.assertRaises(TypeError):
            _ = self.tenner * self.fiver

    def test_name_equality(self):
        self.assertEqual(Name("Harry", "Percival"), Name("Barry", "Percival"))


class TestIdentity(unittest.TestCase):
    def test_barry_is_harry(self):
        harry = Person(Name("Harry", "Percival"))
        barry = harry
        barry.name = Name("Barry", "Percival")
        assert harry is barry and barry is harry


if __name__ == '__main__':
    unittest.main()
