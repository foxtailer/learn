import sqlite3
import os
import aiosqlite
from datetime import datetime

DB_NAME = 'bot_db.db'

async def add_to_udb(user_name, comand_args:str, script_dir):

    connection = sqlite3.connect(f"{script_dir}/{DB_NAME}")
    cursor = connection.cursor()

    today_date = datetime.today().isoformat()[:10]

    data = comand_args.split(',')

    if (len(data) % 3) != 0:
        return False

    data_sets = [tuple(data[i:i + 3]) for i in range(0, len(data), 3)]

    for i in data_sets:
        insert_data = *i, today_date
        cursor.execute(f'INSERT OR REPLACE INTO {user_name} (eng, rus, example, day) VALUES (?, ?, ?, ?)', insert_data)

    connection.commit()
    connection.close()
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


    # Fullfill user table
    import asyncio

    data = 'cat,кот,beautiful cat,believe,вірити,i dont care if you believe in me,again,знову,i just wanna hear your scream again,over,закінчено,game over,around,навколо,beautiful world around us,vargant,бродяга,and vargant ronin Jin,tempestuous,бурный,tempestuous temperament,beheading,обезглавливание,will be executed by beheading,regret,сожаления,feling any regret,held,держать,what held you idiot?,dumplings,пельмени,Hey arent my dumplings ready yet?,frown,хмурится,come on dont give me that frown,governor,губернатор,that blond boy is the son of the prefectural governor,supposed,предпологаемый,whats this supposed to be?,rid,избавлять,go and get rid of that insolent peasant,insolent,наглый,go and get rid of that insolent peasant,peasant,крестьянин,go and get rid of that insolent peasant,fuss,суета,dont make a fuss,interfere,вмешиватся,are you trying to interfere?,bidding,приказы,to serve your lord and do his bidding ... is this honor?,hone,точильный камень,is that what you spend all those years hone your skills for?,worthless,бесполезный,to be blunt I think youre worthless,blunt,прямой тупой,to be blunt I think youre worthless,worth,цена,jeez your lives aint worth squat,squat,приседать,jeez your lives aint worth squat,moron,придурок,what are you some kind of moron,folk,народ,folk s who lay a finger on me pay the price,payroll,зп,my old mans got Yagyu on his payroll right now,recently,недавно,they died just recently,celestial,небесный,the celestial beauty of music,died,помер,they died from,fairytale,казка,pick,вибрати,dreaming,мріяти,scream,кричати,spent,втрачено,deceiving,обманювати,still,досі,tease,дразнити,wrong,неправильно,whaterver,що завгодно,faded,вицвілий,above,вище,wake,розбудити,gone,пішов,wise,мудрий,made,зробив,poor,бідний,stealing,крадіжки,bling men,шикарний чоловік,sick,хворий,'
    asyncio.run(add_to_udb("Victoria", data, find_path()))