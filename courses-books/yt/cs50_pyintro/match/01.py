name = input("Wat's your name? ")

match name:
    case "Harry" | "Hernione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
