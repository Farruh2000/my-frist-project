import psycopg2

db_params={
    'database':'new_list',
    'user':'postgres',
    'possword':'1',
    'host':'localhost',
    'port':'5432',
}


class Book:
    def __init__(self,db_params):
        self.conn = psycopg2.connect(**db_params)
        self.cur = self.conn.cursor()


    def __enter__(self):
        self.cur.execute('''CREATE TABLE if NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,)''')
        self.conn.commit()
        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cur.close()

    def insert_book(self,name,description,author):

        insert_into_query='''INSERT INTO book (name,description,author)
                             VALUES (%s,%s,%s);'''
        self.cur.execute(insert_into_query,(book.name,book.description,book.author))
        self.conn.commit()


    def red_book(self):
        red_query="""SELECT * FROM book ORDER BY id DESC LIMIT 1;"""
        self.cur.execute(red_query)
        return self.cur.fetchall()

    def updet_book(self,book_id):
        updet_query='''UPDATE book SET name=%s;'''
        db_params.append(book_id)
        self.cur.execute(updet_query,book_id)
        self.conn.commit()

    def delete(self,book_id):
        delete_query="""DELETE FROM book WHERE id=%s;"""
        self.cur.execute(delete_query,book_id)

with Book(db_params) as book:
    book.insert_book('O\'tkan kunlar','badiy asar','Abdulla Qodiriy')

    book=book.red_book()
    for i in book:
        print(i)

    book.updet_book(1)

    book.delete(1)
