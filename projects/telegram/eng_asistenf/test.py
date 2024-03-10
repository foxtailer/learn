import sqlite3

# a = """cat,кот,beautiful cat
# believe,вірити,i dont care if you believe in me
# again,знову,i just wanna hear your scream again
# over,закінчено,game over
# around,навколо,beautiful world around us
# vargant,бродяга,and vargant ronin Jin
# tempestuous,бурный,tempestuous temperament
# beheading,обезглавливание,will be executed by beheading
# regret,сожаления,feling any regret
# held,держать,what held you idiot?
# dumplings,пельмени,Hey arent my dumplings ready yet?
# frown,хмурится,come on dont give me that frown
# governor,губернатор,that blond boy is the son of the prefectural governor
# supposed,предпологаемый,whats this supposed to be?
# rid,избавлять,go and get rid of that insolent peasant
# insolent,наглый,go and get rid of that insolent peasant
# peasant,крестьянин,go and get rid of that insolent peasant
# fuss,суета,dont make a fuss
# interfere,вмешиватся,are you trying to interfere?
# bidding,приказы,to serve your lord and do his bidding ... is this honor?
# hone,точильный камень,is that what you spend all those years hone your skills for?
# worthless,бесполезный,to be blunt I think youre worthless
# blunt,прямой тупой,to be blunt I think youre worthless
# worth,цена,jeez your lives aint worth squat
# squat,приседать,jeez your lives aint worth squat
# moron,придурок,what are you some kind of moron
# folk,народ,folk s who lay a finger on me pay the price
# payroll,зп,my old mans got Yagyu on his payroll right now
# recently,недавно,they died just recently
# celestial,небесный,the celestial beauty of music
# died,помер,they died from
# fairytale,казка
# pick,вибрати
# dreaming,мріяти
# scream,кричати
# spent,втрачено
# deceiving,обманювати
# still,досі
# tease,дразнити
# wrong,неправильно
# whaterver,що завгодно
# faded,вицвілий
# above,вище
# wake,розбудити
# gone,пішов
# wise,мудрий
# made,зробив
# poor,бідний
# stealing,крадіжки
# bling men,шикарний чоловік
# sick,хворий"""

# list_of_words = a.split("\n")
# low = [x.split(",") for x in list_of_words]

# data2 = []
# data3 = []
# for i in low:
#     if len(i)==2:
#         data2.append(i)
#     else:
#         data3.append(i)

# connection = sqlite3.connect(r'E:\GIT\projects\telegram\eng_asistenf\Mari.db')
# cursor = connection.cursor()

# for i in data3:
#     cursor.execute(f'INSERT INTO Mari (eng, rus, example) VALUES (?, ?, ?)', tuple(i))

# for i in data2:
#     cursor.execute(f'INSERT INTO Mari (eng, rus) VALUES (?, ?)', tuple(i))

# connection.commit()
# connection.close()

####################################3

# from datetime import datetime
# _path = "E:\\GIT\\projects\\telegram\\eng_asistenf\\"
# user_name = "Simada"
# string = "test,test,test"

# connection = sqlite3.connect(f"{_path}{user_name}.db")
# cursor = connection.cursor()

# cursor.execute(f'SELECT active_days FROM {user_name}_inf')
# user_active_days = cursor.fetchall()
# today_date = datetime.today().strftime("%d/%m/%Y")

# data_to_add = string.strip().lower().split(",")
# data_to_add.append(len(user_active_days))
# print(tuple(data_to_add))

# if today_date == user_active_days[-1][0]:
#     data_to_add = string.strip().lower().split(",").append(len(user_active_days))
# else:
#     data_to_add = string.strip().lower().split(",").append(len(user_active_days)+1)
#     cursor.execute(f'INSERT OR IGNORE INTO {user_name}_inf (days) VALUES (?)', (today_date,))

# cursor.execute(f'INSERT OR IGNORE INTO {user_name} (eng, rus, example, day) VALUES (?, ?, ?, ?)', data_to_add)

# connection.commit()
# connection.close()

###################3333333333333

connection = sqlite3.connect(r"E:\GIT\projects\telegram\eng_asistenf\Simada.db")
cursor = connection.cursor()

#cursor.execute("ALTER TABLE Simada_inf ADD COLUMN test_days TEXT")
cursor.execute(f'INSERT INTO Simada_inf (test_days) VALUES (?)', (0,))

connection.commit()
connection.close()
