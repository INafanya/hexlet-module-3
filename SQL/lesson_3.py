import psycopg2
from psycopg2.extras import execute_batch, execute_values

# Создаем соединение с базой
# hexlet_test - Имя базы данных
try:
    conn = psycopg2.connect("postgresql://userdb:user@localhost:5432/hexlet")
    print(conn)
    # пытаемся подключиться к базе данных
    # conn = psycopg2.connect(
    #     dbname="hexlet", user="user", password="user", host="localhost"
    # )

except:
    print("Can`t establish connection to database")


with conn.cursor() as curs:
    users = [
    ("Bob", "bob@mail.com"),
    ("Alice", "alice@mail.com"),
    ("John", "john@mail.com"),
    ]
    execute_values(curs, "INSERT INTO users (username, email) VALUES %s", users)
    # execute_values(curs, "INSERT INTO users (username, email) VALUES %s RETURNING id", users)
    # print(curs.fetchall())
    conn.commit()