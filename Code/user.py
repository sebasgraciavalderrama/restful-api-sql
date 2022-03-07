import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
         # Instead of using self in the parameters of the method, we use 'cls' since it is.
         # a classmethod.
        connection = sqlite3.connect('Python.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone() # Returns the first result of the query, if there are not results returns None
        if row:
            # row[0] -> id
            # row[1] -> username
            # row[2] -> password
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        # Instead of using self in the parameters of the method, we use 'cls' since it is.
        # a classmethod.
        connection = sqlite3.connect('Python.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone() # Returns the first result of the query, if there are not results returns None
        if row:
            # row[0] -> id
            # row[1] -> username
            # row[2] -> password
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

