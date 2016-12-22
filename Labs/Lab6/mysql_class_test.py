import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset = "utf8"
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class User:

    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO user (name, description) VALUES (%s, %s);",
                  (self.name, self.description))
        self.db_connection.commit()
        c.close()

    def get(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * FROM user;")
        users = []
        for row in c.fetchall():
            u = User
            u.name = row[1]
            u.description = row[2]
            users.append(u)
        return users


class Airlines:

    def __init__(self, db_connection, name, description, flight_id):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description
        self.flight_id = flight_id

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO my_app_airlines2 (name, description, flight_id) VALUES (%s, %s, %s);",
                  (self.name, self.description, self.flight_id))
        self.db_connection.commit()
        c.close()

    def get(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * FROM my_app_airlines2;")
        users = []
        for row in c.fetchall():
            u = User
            u.name = row[1]
            u.description = row[2]
            users.append(u)
        return users



con = Connection("alex", "123", "first_db")

with con:
    user = User(con, 'Санек'.encode('utf-8'), 'Крутой чел'.encode('utf-8'))
    user.save()
    airlines = Airlines(con, 'Аэрофлот', "Российские авиалинии. Москва - Казань", 6634)
    airlines2 = Airlines(con, 'S7', 'Сибирские авиалинии. Москва - Ставрополь ', 5640)
    airlines3 = Airlines(con, 'ПитерАвиа', 'Северные авиалинии. Питер - Казань ', 7009)
    airlines2.save()
    airlines3.save()