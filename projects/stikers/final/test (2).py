import pandas
import datetime

# year, month, day
date = datetime.datetime.now()
carent_date = f"{date.day}:{date.month}:{date.year}"
# 20.01.2023   last change!
MAIN_LIST = ["110","100","150","210","200","250","310","300","350","710","700","750","800","900","950","3050","3150","3300","3450","3600","3750","3900","4150","4400","4250","4350","90402S","90202S","90502S","90102S","90602S","90302S","21301S","21002S","20902S","8500S","8400S","60601S","102S","10401S","10501S","10201S","10301S","10101S","101S","4550S","4500S","30501S","6900S","6800S","6700S","6500S","100 ETL B","700 ETL B","5001","5000","5100","5200","5300","5400","5500","5600","5700","5800","5901","5900","6000","6100","6500","6800","6900","7000","7300","7500","9200","1001","1003","7800","9400","2017","9600","7700","11100","1005","4800","8000","8100","8200","8300","8400","4900","4910","4700","4500","4550","410","400","450","9500","9510","510","500","550","9550","9551","6200","610","600","650","9700","9710","9900","1300","1350","6300","9800","1510","1500","1550","6400","6410","7600","1600","6600","2104","2004","2450","2006","2008","2014","2015","2020","2021","Н060","Н069","Н075","Н070","Н071","21200S","21102S","1005S","70601S","2007S","21601S","90702S","21401S","9550S","21501S","20802S","30502S","103S","2006S","2008S","1007","3101","100В","200В","300В","700В","2014В","2020В","2009В","1900В","1800В","2001В","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2036","81736","2502","10255","2465","10262","9853","9808","8016","7606","4704","6609","1651","1613","1620","1637","1644","1668","1675","1682","1699","1446","1453","1422","1439","81248","10767","10750","9752","1700","1800","1900","2012","2016","2500","1004","2022","TRX 2 ","Melaniq","DRM 4","Immune +"]
BLANK = [0] * len(MAIN_LIST)
now = []; need = []; in_list = []; name = []; last_order = []
dt = 0
def read_data():
    global now, need, in_list, name, last_order, dt
    dt = pandas.read_csv("C:\\Users\\User\\Desktop\\stikers\\final\\_data.csv")
    # name	inList	now	minn order
    now = dt.now.to_list()
    need = dt.minn.to_list()
    in_list = dt.inList.to_list()
    name = dt.name.to_list()
    last_order = dt["last order"].to_list()

articuls_list = []; amounts_list = []
def read_from_1c():
    
    """Open files with colum from 1C and sort them for MAIN_LIST.
    After sort print amounts
    """
    global articuls_list, amounts_list
    with open(r"C:\Users\User\Desktop\stikers\final\articuls.txt", encoding="utf-8") as articuls_file:
        data = articuls_file.readlines()
        articuls_list = [line.strip() for line in data]

    with open(r"C:\Users\User\Desktop\stikers\final\amounts.txt", encoding="utf-8") as amounts_file:
        data = amounts_file.readlines()
        amounts_list = [int(line.strip().replace(",000", "")) for line in data]


order = []
def print_order():
    for i in range(len(now)):
        if now[i] < need[i] and now[i] > 0:
            if need[i] < in_list[i]:
                order.append(1)
            else:
                order.append(need[i]//in_list[i] + 1)
        else:
            order.append(0)

    for i in range(len(order)):
        if order[i] > 0:
            print(f"{name[i]} ({order[i]});")

minus_list = []
def minus_generate():
    for articul in articuls_list:
        if articul not in MAIN_LIST:
            print(articul, "NOT IN MAIN LIST!!!")
    for articul in MAIN_LIST:
        if articul in articuls_list:
            minus_list.append(int(amounts_list[articuls_list.index(articul)]))
        else:
            minus_list.append(0)

def minus():
    for i in range(len(now)):
        now[i] -= minus_list[i]


read_from_1c()
read_data()
minus_generate()
minus()
print_order()

dt[f"order{carent_date}"] = last_order
dt["now"] = now
dt.to_csv("data.csv", index=False)

# amounts to lists
# for i in range(len(now)):
#     try:
#         print(f"{name[i]} ({(now[i]/in_list[i]).round(2)})")
#     except:
#         print(f"{name[i]} ({now[i]}/{in_list[i]})")