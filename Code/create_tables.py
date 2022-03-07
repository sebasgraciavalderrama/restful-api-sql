# We call this script to create tables, nothing else.
import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

delete_query = "DROP TABLE IF EXISTS users"
cursor.execute(delete_query)

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cursor.execute(create_table)

connection.commit()
connection.close()