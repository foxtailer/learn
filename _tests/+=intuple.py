data = (["a"], 'py')

data[0] += ["b"]  # equal to data[0] = data[0] + ["b"]
# prev lina qual to 2 step expression 
# 1: data[0] + ["b"]  work and modify list
# 2: data[0] = result of first step >>> Error 
# Tuple does not support item assignment

print(data)

try:
    data = (["a"], 'py')
    data[0] += ["b"]
except:
    print(data)  # >>> (["a", "b"], "py")