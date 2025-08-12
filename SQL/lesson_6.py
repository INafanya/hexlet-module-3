import psycopg2
from psycopg2.extras import DictCursor

try:
    conn = psycopg2.connect("postgresql://userdb:user@localhost:5432/hexlet")
except:
    print("Can`t establish connection to database")
    
    
# def create_post(conn, post_dic):
#     with conn.cursor() as curs:
#         insert_query = """
#         INSERT INTO posts (title, content, author_id) VALUES (%s, %s, %s) RETURNING id;
#         """
#         values = [post_dic['title'], post_dic['content'], post_dic['author_id']]
#         curs.execute(insert_query, values)
#         post_id = curs.fetchone()[0]
#         conn.commit()
#     return post_id


# def add_comment(conn, comment_dic):
#     with conn.cursor() as curs:
#         insert_query = """
#         INSERT INTO comments (post_id, author_id, content) VALUES (%s, %s, %s) RETURNING id;
#         """
#         values = [comment_dic['post_id'], comment_dic['author_id'], comment_dic['content']]
#         curs.execute(insert_query, values)
#         comment_id = curs.fetchone()[0]
#         conn.commit()
#     return comment_id


def get_latest_posts(conn, posts_count):
    with conn.cursor(cursor_factory=DictCursor) as curs:
        # posts = []
        sql = """
        SELECT id, title, content, author_id, created_at
        from posts
        limit %s;
        """
        with conn.cursor() as curs:
            curs.execute(sql, (posts_count,))
            result = curs.fetchall()
        conn.commit()
        return result
        # curs.execute(sql, (posts_count,))
        # posts = curs.fetchall()
        # for row in curs:
        #     posts.append(row)
        # posts.append(curs.fetchone())
        # return posts

print(get_latest_posts(conn, 1))
# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# post_id = 5#create_post(conn, post)
# print(post_id)
# comment_1 = {'post_id': post_id, 'author_id': 42, 'content': 'wow such post'}
# comment_2 = {'post_id': post_id, 'author_id': 24, 'content': 'totally disagree btw i use arch'}

# comment_id = add_comment(conn, comment_2)
# print(comment_id)

# print(get_latest_posts(conn, 5))



