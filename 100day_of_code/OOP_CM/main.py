from menu import Menu, MenuItem
from moneymachine import MoneyMachine
from coffemaker import CoffeMaker

class CoffeMachine():

    def __init__(self) -> None:
        self._on = True
        self._menu = Menu()
        self._moneymachine = MoneyMachine(0)
        self._coffemaker = CoffeMaker()

    def is_on(self):
        while self._on:
            print("What would you like?")
            self._menu.get_items()
            choice = input()

            if choice == "off":
                self._on = False
            elif choice == "moneyreport":
                self._moneymachine.report()
            elif choice == "resoursereport":
                self._coffemaker.report()
            else:
                if self._menu.find_drink(choice) and\
                    self._moneymachine.make_payment(self._menu.find_cost(choice)) and\
                    self._coffemaker.is_resource_sufficient(self._menu.find_drink(choice)):
                        print(f"Enjoy your {choice}!")

                

lavaza333 = CoffeMachine()
lavaza333.is_on()
