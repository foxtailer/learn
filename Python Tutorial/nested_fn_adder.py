# Task 1 "adder"
# adder(5)(3) -> 8
def adder(x,y=[]):
    if y:
        result = x + y[0]
        y.clear()
        return result
    else:
        y.append(x)
        return adder 

print(adder(4)(4))
print(adder(2)(2))
print(adder(1)(1))

print("******")

def adder2(x):
    def wrapper(y):
        return x + y
    return wrapper

print(adder2(4)(4))
print(adder2(2)(2))
print(adder2(1)(1))