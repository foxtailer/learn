temp = {}
for i in open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\_tests\count_unick_items\data.txt"):
    i = i.strip()
    if i not in temp.keys():
        temp[i]=1
    else:
        temp[i]+=1

with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\_tests\count_unick_items\result.txt", "a") as f:
    for k, v in temp.items():
        f.write(f"{k} {v}\n")
