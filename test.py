fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(4)
except IndexError:
    print("Not existing index")
    make_pie(int(input("Try ather index: ")))