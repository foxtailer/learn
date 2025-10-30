def exchange(denominations: list[int], amount:int):
    bills = []
    
    for den in denominations:
        num_of_bills = amount // den
        bills.append(num_of_bills)
        amount -= num_of_bills * den

    return bills


denominations = [300, 200, 100, 50, 20, 10, 5, 2, 1]
amount = 257

ex = exchange(denominations, amount)

print(ex)                
                
assert len(denominations) == len(ex)
assert sum([a*b for a, b in zip(denominations, ex)]) == amount

