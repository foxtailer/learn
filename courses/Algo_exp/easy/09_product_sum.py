def product_sum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += product_sum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier


array = [5,2,[7,-1],3,[6,[-13,8],4]]
print(product_sum(array))
