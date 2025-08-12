import psycopg2
from psycopg2.extras import execute_batch, execute_values

try:
    conn = psycopg2.connect("postgresql://userdb:user@localhost:5432/hexlet")
    print(conn)
except:
    print("Can`t establish connection to database")

def batch_insert(conn, products):
    with conn.cursor() as curs:
        values = [(p['name'], p['price'], p['quantity']) for p in products]
        insert_query = "INSERT INTO products (name, price, quantity) VALUES %s"
        curs.execute(insert_query, values)
        conn.commit()


def get_all_products(conn):
    sql = "SELECT * FROM products ORDER BY price DESC;"
    with conn.cursor() as curs:
        curs.execute(sql)
        result = curs.fetchall()
    conn.commit()
    return result

products = [
        {'name': 'apple', 'price': 5, 'quantity': 10},
        {'name': 'kiwi', 'price': 7, 'quantity': 12},
        {'name': 'cheese', 'price': 15, 'quantity': 20},
        {'name': 'butter', 'price': 10, 'quantity': 8}
    ]

batch_insert(conn, products)