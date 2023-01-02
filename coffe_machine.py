# homePC add
# home laptop add

turn_on = True
resources = {"Water":{"value":1000, "unit":"ml"}, "Milk":{"value":300, "unit":"ml"},\
"Coffe":{"value":100, "unit":"g"}, "Money":{"value":0, "unit":"$"}}
ESPRESO_COST = 100,0,10,1
LATTE_COST = 100,50,10,1
CAPPUCCINO_COST = 100,100,10,1

def check(drink):
    report = []
    i = 0
    for item in resources.items():
        if i > 2:
            break
        if item[1]["value"] < drink[i]:
            report.append(item[0])
        i += 1
    return report

def subtract(drink):
    resources["Water"]["value"] -= drink[0]
    resources["Milk"]["value"] -= drink[1]
    resources["Coffe"]["value"] -= drink[2]

def insert_coins(drink):
    amount = 0

    while True:
        coins = input("Insert coins pls >>> ").split()

        for i in coins:
            if i == "quarter":
                amount += 0.25
            elif i == "dimes":
                amount += 0.1
            elif i == "nickles":
                amount += 0.05
            elif i == "pennies":
                amount += 0.01

        if amount < drink[3]:
            print("Sorry that's not enough money. Money refunded.")
        elif amount > drink[3]:
            print(f"Here is ${amount - drink[3]:.2f} dollars in change.")
            resources["Money"]["value"] += drink[3]
            return True
        else:
            resources["Money"]["value"] += drink[3]
            return True

        

while turn_on:
    user_choise = input("What would you like? (espresso/latte/cappuccino): ")

    #while True:
    if user_choise == "espresso" or user_choise == "1":
        x = check(ESPRESO_COST)
        if not x and insert_coins(ESPRESO_COST):
            print('Here is your espresso. Enjoy!')
            subtract(ESPRESO_COST)
        else:
            print(f"Sorry there is not enough {', '.join(x)}.")
        break

    elif user_choise == "latte" or user_choise == "2":
        x = check(LATTE_COST)
        if not x and insert_coins(LATTE_COST):
            print('Here is your latte. Enjoy!')
            subtract(LATTE_COST)
        else:
            print(f"Sorry there is not enough {', '.join(x)}.")
        break

    elif user_choise == "cappuccino" or user_choise == "3":
        x = check(CAPPUCCINO_COST)
        if not x and insert_coins(CAPPUCCINO_COST):
            print('Here is your cappuccino. Enjoy!')
            subtract(CAPPUCCINO_COST)
        else:
            print(f"Sorry there is not enough {', '.join(x)}.")
        break

    elif user_choise == "off":
        turn_on = False
        break

    elif user_choise == "report":
        for item in resources.keys():
            print(f"{item}: {resources[item]['value']}{resources[item]['unit']}")
        break
    
    else:
        user_choise = input("Pls chuse one of this:\nespresso/latte/cappuccino\n")







