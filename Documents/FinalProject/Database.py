import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()

    def register(self, name, username, password):
        sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, username, password))
        self.db.commit()

    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        user = self.cursor.fetchone()
        return user