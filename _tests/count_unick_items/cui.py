temp = {}
for line in open(r"./data.txt"):
    line = line.strip()
    if line not in temp:
        temp[line]=1
    else:
        temp[line]+=1

with open(r"./result.txt", "a") as file:
    for line, emount in temp.items():
        file.write(f"{line} {emount}\n")
