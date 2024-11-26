def suf(a):
    p = [0]*len(a)
    j=0
    i=1

    while i<len(a):
        if a[j] == a[i]:
            j+=1
            p[i] = j+1
            i+=1
            
        else:
            if j == 0:
                p[i] = 0
                i+=1
            else:
                j = p[j-1]
    
    return p

def substr(s, a):
    i=0
    j=0

    p = suf(s)

    while i<len(a):
        if a[i] == s[j]:
            i+=1
            j+=1
            if j == len(s):
                print("+")
                print(i-j)
                break
        else:
            if j>0:
                j = p[j-1]
            else:
                i+=1
    if i == len(a):
        print('-')

a = 'lililos lililas'
s = 'lilila'

print(suf(s))
substr(s,a)

