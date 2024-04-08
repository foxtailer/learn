def solution(s):
    if len(s)2 == 0:
        return [s[x:x+2] for x in range(0,len(s),2)]
    else:
        s = s+"_"
        return [s[x:x+2] for x in range(0,len(s),2)]


print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))

