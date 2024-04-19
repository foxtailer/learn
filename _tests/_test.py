def scramble(s1, s2):
    s1_dict = {}
    for i in s1:
        try:
            s1_dict[i] += 1
        except:
            s1_dict[i] = 1

s1 = "aafngekke"
s1_dict = {}
for i in s1:
    try:
        s1_dict[i] += 1
    except:
        s1_dict[i] = 1
print(s1_dict)