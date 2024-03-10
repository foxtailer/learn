import sqlite3
from datetime import datetime

_path = "E:\\GIT\\projects\\telegram\\eng_asistenf\\"


async def add_to_udb(user_name, string):

    connection = sqlite3.connect(f"{_path}{user_name}.db")
    cursor = connection.cursor()

    cursor.execute(f'SELECT active_days FROM {user_name}_inf')
    user_active_days = cursor.fetchall()
    today_date = datetime.today().strftime("%d/%m/%Y")

    if today_date == user_active_days[-1][0]:
        data_to_add = string.strip().lower().split(",")
        data_to_add.append(len(user_active_days))
    else:
        data_to_add = string.strip().lower().split(",")
        data_to_add.append(len(user_active_days)+1)

        cursor.execute(f'INSERT OR IGNORE INTO {user_name}_inf (days) VALUES (?)', (today_date,))

    cursor.execute(f'INSERT OR IGNORE INTO {user_name} (eng, rus, example, day) VALUES (?, ?, ?, ?)', tuple(data_to_add))

    connection.commit()
    connection.close()

async def del_from_udb(user_name, string):
    data_to_del = tuple(string.strip().lower().split(","))
    if len(data_to_del) == 1:
        data_to_del = f"({data_to_del[0]})"

    connection = sqlite3.connect(f"{_path}{user_name}.db")
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM {user_name} WHERE id IN {data_to_del}')

    connection.commit()
    connection.close()


async def addm_to_udb(user_name, string):
    list_of_words = string.split(",")
    eng = [word for word in list_of_words[::2]]
    rus = [word for word in list_of_words[1::2]]

    connection = sqlite3.connect(f"{_path}{user_name}.db")
    cursor = connection.cursor()

    cursor.execute(f'SELECT active_days FROM {user_name}_inf')
    user_active_days = cursor.fetchall()
    today_date = datetime.today().strftime("%d/%m/%Y")

    if today_date == user_active_days[-1][0]:
        for i in range(len(eng)):
            data = eng[i], rus[i], len(user_active_days)
            cursor.execute(f'INSERT INTO {user_name} (eng, rus, day) VALUES (?, ?, ?)', data)
    else:
        for i in range(len(eng)):
            data = eng[i], rus[i], len(user_active_days)+1
            cursor.execute(f'INSERT INTO {user_name} (eng, rus, day) VALUES (?, ?, ?)', data)

    connection.commit()
    connection.close()

async def create_csv(user_name):
    connection = sqlite3.connect(f"{_path}{user_name}.db")
    cursor = connection.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {user_name} (
            id INTEGER PRIMARY KEY,
            eng TEXT NOT NULL,
            rus TEXT NOT NULL,
            example TEXT,
            day INTEGER
        )
    """)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {user_name}_inf (
            active_days TEXT
        )
    """)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {user_name}_test (
            test_days TEXT
        )
    """)

    today_date = datetime.today().strftime("%d/%m/%Y")

    cursor.execute(f'INSERT OR IGNORE INTO {user_name}_inf (active_days) VALUES (?)', (today_date,))
    cursor.execute(f'INSERT INTO {user_name}_test (test_days) VALUES (?)', (0,))

    #cursor.execute(f'CREATE INDEX idx_eng ON {user_name} (eng)')
    connection.commit()
    connection.close()


async def check_user(user_name:str)->bool:

    """Check if username in list of users and add if not"""

    with open(f"{_path}users.txt", "r") as users:
        list_of_users = [name.strip() for name in users.readlines()]
        
    if user_name not in list_of_users:
        with open(f"{_path}users.txt", "a") as users:
            users.write("\n"+user_name)
            await create_csv(user_name)
        return False
    else:
        return True

def transfer(a, b, name):
    connection = sqlite3.connect(a)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {name}')
    user_dict = cursor.fetchall()
    user_dict = [tuple(list(x)[1:]) for x in user_dict]

    connection.commit()
    connection.close()

    connection = sqlite3.connect(b)
    cursor = connection.cursor()

    for i in user_dict:
        print(i)
        cursor.execute(f'INSERT INTO {name} (eng, rus, example, day) VALUES (?, ?, ?, ?)', i)

    connection.commit()
    connection.close()

#transfer(r"E:\GIT\projects\telegram\eng_asistenf\Simada2.db", r"E:\GIT\projects\telegram\eng_asistenf\Simada.db", "Simada")
# connection = sqlite3.connect(r"E:\GIT\projects\telegram\eng_asistenf\Simada.db")
# cursor = connection.cursor()

# #cursor.execute(f'DELETE FROM Simada_inf')
# # for i in [("15/02/2024",), ("16/02/2024",)]:
# #     cursor.execute(f'INSERT INTO Simada_inf (active_days) VALUES (?)', i)

# cursor.execute(f'UPDATE Simada SET day=2 WHERE day=4')

# connection.commit()
# connection.close()