import psycopg2
from psycopg2.extras import DictCursor

try:
    conn = psycopg2.connect("postgresql://userdb:user@localhost:5432/hexlet")
except:
    print("Can`t establish connection to database")


def get_order_sum(conn, month):
    template = "Покупатель {name} совершил покупок на сумму {total}".format
    with conn.cursor(cursor_factory=DictCursor) as curs:
        sql = """select usr.customer_name, sum(ord.total_amount) as total
        from orders ord
        left join customers usr on ord.customer_id = usr.customer_id
        where EXTRACT(MONTH FROM order_date) = %s
        group by usr.customer_name;
        """
        curs.execute(sql, (month,))
        result = []
        for row in curs:
            name = row['customer_name']
            total = row['total']
            result.append(template(name=name, total=total))
    conn.commit()
    return '\n'.join(result)
    
print(get_order_sum(conn, 2))
