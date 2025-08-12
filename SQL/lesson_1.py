import psycopg2

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

    sql = "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), phone VARCHAR(255));"
    # Запрос выполняется через создание объекта курсора
    cursor = conn.cursor()
    cursor.execute(sql) # Коммитим, т.е. сохраняем изменения в БД
    cursor.close()  # в конце закрывается

    # sql2 = "INSERT INTO users (username, phone) VALUES ('tommy', '123456789');"
    # cursor = conn.cursor()
    # cursor.execute(sql2)
    # conn.commit()
    # cursor.close()

    # sql3 = "SELECT * FROM users;"
    # cursor = conn.cursor()
    # # Указатель на набор данных в памяти СУБД
    # cursor.execute(sql3)
    # for row in cursor:
    #     print(row)
    # cursor.close()
    conn.close() 
    print('OK')# Соединение нужно закрыть