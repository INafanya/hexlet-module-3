import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def get_all_cars(conn):
    sql = """
    SELECT
        id,
        brand,
        model
    FROM cars
    ORDER BY brand;
    """
    with conn.cursor() as curs:
        curs.execute(sql)
        result = curs.fetchall()
    return result
# END