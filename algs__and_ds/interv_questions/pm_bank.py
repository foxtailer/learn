from threading import Lock, Thread
from venv import logger
from decimal import Decimal


class Account:
    def __init__(self, money):
        self._money = money

    @property
    def money(self) -> int:
        return self._money
    
    @money.setter
    def money(self, value: int) -> None:
        self._money = value


class MoneyTransfer:
    
    def __init__(self, lock: Lock) -> None:
        self._lock: Lock = lock

    def transfer(self, from_account: Account,
                 to_account: Account,
                 amount: float):
        with self._lock:
            try:
                from_account.money -= amount
            except ValueError:
                logger.warning('Invalid money count')
                return
            to_account.money += amount


class TestMoneyTransfer:

    def test_transter(self):
        account = Account(Decimal(100))
        account2 = Account(Decimal(100))
        lock = Lock()
        mone_transfer = MoneyTransfer(lock)

        mone_transfer.transfer(account, account2, Decimal(50))

        assert account.money == 50
        assert account2.money == 150


class TestMoneyTransfer:

    def test_transter(self):
        account = Account(Decimal(100))
        account2 = Account(Decimal(100))
        lock = Lock()
        mone_transfer = MoneyTransfer(lock)

        th_1 = Thread(target=mone_transfer.transfer,
                      args=(account, account2, Decimal(50))
                      )
        th_2 = Thread(target=mone_transfer.transfer,
                      args=(account, account2, Decimal(100))
                      )
        th_3 = Thread(target=mone_transfer.transfer,
                      args=(account, account2, Decimal(45))
                      )
        
        mone_transfer.transfer(account, account2, Decimal(50))

        assert account.money == 50
        assert account2.money == 150


test = TestMoneyTransfer()
test.test_transter()
