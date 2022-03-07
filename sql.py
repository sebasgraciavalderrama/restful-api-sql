import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

delete_query = "DROP TABLE IF EXISTS users"
cursor.execute(delete_query)

create_table = "CREATE TABLE IF NOT EXISTS users (id INT, username TEXT, password TEXT)"
cursor.execute(create_table)

users = [
    (1, 'sebas', 'abc123'),
    (2, 'user2', 'abc123'),
    (3, 'user3', 'abc123'),
    (4, 'user4', 'abc123')
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
