class CoffeMachine():
    _on = True
    def is_on(self):
        while self._on:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "off":
                self._on = False
            else:
                print(choice)

lavaza333 = CoffeMachine()
lavaza333.is_on()
