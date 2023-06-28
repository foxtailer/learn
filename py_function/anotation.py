def meow(n: int) -> str:
    """Moew n times"""
    return "Meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
