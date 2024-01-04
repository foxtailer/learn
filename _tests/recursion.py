import sys

def rec(n:int):
    if n == 1:
        var = "*"*n
        print(f"{var:~^10}")
    else:
        var = "*"*n
        print(f"{var:~^10}")
        rec(n-1)
        print(f"{var:~^10}")

rec(5)
print(sys.getrecursionlimit())

s = "ff"
l = 20
print(f"{s:~^20}")
print(f"{s:~<20}")
print(f"{s:~>20}")
print(f"{s:~^{l}}")