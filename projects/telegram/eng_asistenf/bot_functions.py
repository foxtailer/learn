import sqlite3
import os
import aiosqlite
from datetime import datetime

DB_NAME = 'bot_db.db'

async def add_to_udb(user_name: str, comand_args: str, script_dir: str) -> bool:
    db_path = f"{script_dir}/{DB_NAME}"
    
    async with aiosqlite.connect(db_path) as connection:
        async with connection.cursor() as cursor:
            today_date = datetime.today().isoformat()[:10]
            data = comand_args.split(',')

            if (len(data) % 3) != 0:
                return False

            data_sets = [tuple(data[i:i + 3]) for i in range(0, len(data), 3)]

            for i in data_sets:
                insert_data = (*i, today_date)
                await cursor.execute(
                    f'INSERT OR REPLACE INTO {user_name} (eng, rus, example, day) VALUES (?, ?, ?, ?)',
                    insert_data
                )
            
            await connection.commit()  

    return True


async def del_from_udb(user_name, string, script_dir):
    data_to_del = tuple(string.strip().lower().split(","))
    if len(data_to_del) == 1:
        data_to_del = f"({data_to_del[0]})"

    connection = sqlite3.connect(f"{script_dir}/{user_name}.db")
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM {user_name} WHERE id IN {data_to_del}')

    connection.commit()
    connection.close()


async def create_user(user_name: str, script_dir: str) -> None:
    
    async with aiosqlite.connect(f"{script_dir}/{DB_NAME}") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {user_name} (
                    id INTEGER PRIMARY KEY,
                    eng TEXT NOT NULL UNIQUE,
                    rus TEXT NOT NULL,
                    example TEXT,
                    day TEXT,
                    lvl INTEGER DEFAULT 0
                )
            """)
            await conn.commit()


async def check_user(user_name:str, script_dir)->bool:
     
     async with aiosqlite.connect(f"{script_dir}/{DB_NAME}") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM users WHERE name = ?", (user_name,))
            user_exists = (await cursor.fetchone())[0] > 0

            if not user_exists:
                await cursor.execute("INSERT INTO users (name) VALUES (?)", (user_name,))
                await conn.commit()
                await create_user(user_name, script_dir)
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
        cursor.execute(f'INSERT INTO {name} (eng, rus, example, day) VALUES (?, ?, ?, ?)', i)

    connection.commit()
    connection.close()


def find_path():
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)

    return script_dir


# from datetime import datetime

# def iso_to_unix(date_str):
#     dt = datetime.fromisoformat(date_str)
#     return int(dt.timestamp())

# # Example conversion
# date_str = '2023-08-12'
# unix_timestamp = iso_to_unix(date_str)

if __name__ == '__main__':

    db_path = f"{find_path()}/{DB_NAME}"
    print(f"Connecting to database at {db_path}")

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        print("Creating table if not exists...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        
        connection.commit()
        print("Table created or already exists.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        connection.close()
