import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def add_movies(conn):
    sql = "INSERT INTO movies (id, title, release_year, duration) VALUES (1, 'Godfather', 1972, 175), (2, 'The Green Mile', 1999, 189);"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def get_all_movies(conn):
    sql = "SELECT * FROM movies;"
    cursor = conn.cursor()
    cursor.execute(sql)
    return list(cursor)
# END