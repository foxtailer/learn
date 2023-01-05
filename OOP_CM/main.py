from menu import Menu, MenuItem
from moneymachine import MoneyMachine

class CoffeMachine():

    def __init__(self) -> None:
        self._on = True
        self._menu = Menu()
        self._moneymachine = MoneyMachine(0)

    def is_on(self):
        while self._on:
            print("What would you like?")
            self._menu.get_items()
            choice = input()

            if choice == "off":
                self._on = False
            else:
                if self._menu.find_drink(choice):
                    if self._moneymachine.make_payment(self._menu.find_cost(choice)):
                        print("eeeeee")

                

lavaza333 = CoffeMachine()
lavaza333.is_on()
