import sqlite3
from flask_restful import Resource, reqparse

# Definition of classes and methods for each class.
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # The class methods are bound to the class definition rather than its object.
    # Though classmethod and staticmethod are quite similar, there's a slight difference
    # in usage for both entities: classmethod must have a reference to a class object as the
    # first parameter (cls), whereas staticmethod can have no parameters at all.
    @classmethod
    def find_by_username(cls, username):
         # Instead of using self in the parameters of the method, we use 'cls' since it is.
         # a classmethod.
        connection = sqlite3.connect('data.db')
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
        connection = sqlite3.connect('data.db')
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

class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Username field cannot be left blank!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Password field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args() # This is to get username and password from the POST request made in Postman

        if User.find_by_username(data['username']) is not None:
            return {"message": "A user with that username already exists"}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password'])) # Here we catch the username and password from the data made by Postman (line 69....nice)

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201