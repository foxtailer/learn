class MenuItem:
    def __init__(self, name, cost, water, coffe, milk):
        self.name = name
        self.cost = cost
        self.ingredients = {"water" : water,
                            "coffe" : coffe,
                            "milk" : milk
        }


class Menu:
    __PARAM = ('Name','Water','Milk','Coffe','Cost')
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffe=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffe=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffe=24, cost=3),
        ]
    
    def add_item(self):
        new_item = []
        for i in self.__PARAM:
            temp = input(f"Enrer new items {i}: ")
            if temp.isdigit():
                new_item.append(float(temp))
            else:
                new_item.append(temp)
        self.menu.append(MenuItem(*new_item))

    def get_items(self):
        result = ""
        for item in self.menu:
            result += item.name+"/"
        print(result)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return True
        else:
            print("Not available :(")

    def find_cost(self, name):
        for item in self.menu:
            if item.name == name:
                return item.cost
        
            



    
