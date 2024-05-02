class MoneyMachine:

    def __init__(self, money_amount) -> None:
        self.money_amount = money_amount

    def report(self):
        print(f"Money: {self.money_amount}")

    def make_payment(self, cost):
        amount = 0

        while True:
            coins = input("Insert coins pls(quarter, dimes, nickles, pennies)\n>>> ").split()

            for i in coins:
                if i == "quarter":
                    amount += 0.25
                elif i == "dimes":
                    amount += 0.1
                elif i == "nickles":
                    amount += 0.05
                elif i == "pennies":
                    amount += 0.01

            if amount < cost:
                print("Sorry that's not enough money. Money refunded.")
            elif amount > cost:
                print(f"Here is ${amount - cost:.2f} dollars in change.")
                self.money_amount += cost
                return True
            else:
                self.money_amount += cost
                return True
