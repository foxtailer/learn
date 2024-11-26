from concreate import Espresso, Mocha, HouseBlend, Chocolate


if __name__ == "__main__":
    # Start with an Espresso
    beverage = Espresso()
    print(f"{beverage.get_description()} -> ${beverage.cost():.2f}")

    # Add Mocha to the Espresso
    beverage = Mocha(beverage)
    print(f"{beverage.get_description()} -> ${beverage.cost():.2f}")

    # Add another Mocha
    beverage = Mocha(beverage)
    print(f"{beverage.get_description()} -> ${beverage.cost():.2f}")

    # Start with a House Blend
    house_blend = HouseBlend()
    print(f"{house_blend.get_description()} -> ${house_blend.cost():.2f}")

    # Add Mocha to the House Blend
    house_blend = Mocha(house_blend)
    print(f"{house_blend.get_description()} -> ${house_blend.cost():.2f}")

    # Add Chocolate to the House Blend
    house_blend = Chocolate(house_blend)
    print(f"{house_blend.get_description()} -> ${house_blend.cost():.2f}")
   
    # Add another Chocolate to the House Blend
    house_blend = Chocolate(house_blend)
    print(f"{house_blend.get_description()} -> ${house_blend.cost():.2f}")
    