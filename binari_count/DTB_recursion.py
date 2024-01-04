def decimal_to_binary(num):
    if num>=1:
        decimal_to_binary(num//2)
        print(num%2, end="")

def bin_count(num):
    i = 0
    while i<=num:
        decimal_to_binary(i)
        print()
        i+=1

bin_count(17)
