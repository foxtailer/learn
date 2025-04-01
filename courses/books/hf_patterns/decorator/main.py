from concreate import Espresso, Mocha, HouseBlend, Chocolate
from abstract import Size


if __name__ == "__main__":
    # Start with an Espresso
    beverage = Espresso()
    beverage.set_size(Size.MEDIUM)  # Set size to Medium
    print(f"{beverage.get_description()} ({beverage.get_size()}) -> ${beverage.cost():.2f}")

    # Add Mocha to the Espresso
    beverage = Mocha(beverage)
    print(f"{beverage.get_description()} ({beverage.get_size()}) -> ${beverage.cost():.2f}")

    # Add another Mocha
    beverage = Mocha(beverage)
    print(f"{beverage.get_description()} ({beverage.get_size()}) -> ${beverage.cost():.2f}")

    # Start with a House Blend
    house_blend = HouseBlend()
    house_blend.set_size(Size.LARGE)  # Set size to Large
    print(f"{house_blend.get_description()} ({house_blend.get_size()}) -> ${house_blend.cost():.2f}")

    # Add Mocha to the House Blend
    house_blend = Mocha(house_blend)
    print(f"{house_blend.get_description()} ({house_blend.get_size()}) -> ${house_blend.cost():.2f}")

    # Add Chocolate to the House Blend (you need to define Chocolate class similarly to Mocha)
    house_blend = Chocolate(house_blend)
    print(f"{house_blend.get_description()} ({house_blend.get_size()}) -> ${house_blend.cost():.2f}")

    # Add another Chocolate to the House Blend
    house_blend = Chocolate(house_blend)
    print(f"{house_blend.get_description()} ({house_blend.get_size()}) -> ${house_blend.cost():.2f}")

    