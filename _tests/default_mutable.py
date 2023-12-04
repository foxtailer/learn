def extend_list(value, lst=[]):
    lst.append(value)
    return lst
# default list creates only once when fu defined

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list("a")
# list1 and list3 is the same list

print(list1) # >>> [10, "a"]
print(list2) # >>> [123]
print(list3) # >>> [10, "a"]
