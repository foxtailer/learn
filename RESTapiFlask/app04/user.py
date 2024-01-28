import sqlite3
from flask import request

class User():
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def create_db(cls):
        connection = sqlite3.connect('/home/aska/Documents/GIT/learn/RESTapiFlask/app04/data.db')
        cursor = connection.cursor()

        create_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
        cursor.execute(create_query)

        users = [
            ("admin", "admin"),
            ("tom", "tom")
        ]
        insert_query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.executemany(insert_query, users)

        connection.commit()
        connection.close()

        
    @classmethod
    def find_user(cls, username):
        connection = sqlite3.connect('/home/aska/Documents/GIT/learn/RESTapiFlask/app04/data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
    @classmethod
    def post(cls):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = (username, password)

        connection = sqlite3.connect('/home/aska/Documents/GIT/learn/RESTapiFlask/app04/data.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(insert_query, user)

        connection.commit()
        connection.close()
        
        return {"message":user}