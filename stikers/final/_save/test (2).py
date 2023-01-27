import pandas
dt = pandas.read_csv("C:\\Users\\User\\Desktop\\stikers\\final\\data.csv")
# name	inList	now	minn order
order = []
now = dt.now.to_list()
need = dt.minn.to_list()
in_list = dt.inList.to_list()
name = dt.name.to_list()

for i in range(len(now)):
    if now[i] < need[i]:
        if need[i] < in_list[i]:
            order.append(1)
        else:
            order.append(need[i]//in_list[i] + 1)
    else:
        order.append(0)

for i in range(len(order)):
    if order[i] > 0:
        print(f"{name[i]} ({order[i]});")

