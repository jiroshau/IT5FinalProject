import mysql.connector
class Database:
    __user = None
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
        sql = f"INSERT INTO users (name, username, password) VALUES ('{name}', '{username}', '{password}')"
        self.cursor.execute(sql)
        self.db.commit()
 
    def login(self, username, password):
        sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(sql) 
        user = self.cursor.fetchone()
        self.__user = user
        return user