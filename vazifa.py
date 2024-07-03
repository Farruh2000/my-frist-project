import psycopg2

conn= psycopg2.connect(database="new_list",
                        user="postgres",
                        password="1",
                        host="localhost",
                        port="5432")
# cur = conn.cursor()
# create_table_userrs = """CREATE TABLE IF NOT EXISTS userrs(
#     id serial  PRIMARY kEY,
#     frst_name  VARCHAR(255)NOT NULL,
#     last_name  VARCHAR(255)NOT NULL,
#     age        INT NOT NULL CHECK(age>0),
#     phone      VARCHAR(13)NOT NULL,
#     create_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
# """
#
# cur.execute(create_table_userrs)
# conn.commit()
# cur.close()
# conn.close()
class userrs:
    def __init__(self,frst_name:str,
                 last_name:str,
                 age:int,
                 phone:str,
                 ):
        self.frst_name = frst_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    conn = psycopg2.connect(database="new_list",
                            user="postgres",
                            password="1",
                            host="localhost",
                            port="5432")
    @staticmethod
    def save(self):
        cur = conn.cursor()
        insert_query = ("""INSERT INTO userrs(frst_name,last_name,age,phone)
        VALUES(%s,%s,%s,%s)""")

        cur.execute(insert_query,(self.frst_name,self.last_name,self.age,self.phone))
        self.id =cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        @staticmethod
        def get_userr(userrs_id=None):
            conn = psycopg2.connect(database="new_list",
                                    user="postgres",
                                    password="1",
                                    host="localhost",
                                    port=5432)


            cur = conn.cursor()
            select_query="""SELECT * FROM userrs WHERE id=%s"""
            cur.execute(select_query,(userrs_id,))
            userrs = cur.fetchall()
            cur.close()
            conn.close()
            return userrs

        @staticmethod
        def dalete_userrs(userrs_id):
            conn = psycopg2.connect(database="new_list",
                                    user="postgres",
                                    password="1",
                                    host="localhost",
                                    port="5432")
            cur = conn.cursor()
            delete_query = """delete from userrs where id=%s"""
            cur.execute(delete_query,(userrs_id,))
            conn.commit()
            cur.close()
            conn.close()


            @staticmethod
            def update_userrs(self,userrs_id):
                conn = psycopg2.connect(database="new_list",
                                        user="postgres",
                                        password="1",
                                        host="localhost",
                                        port="5432")
                cur = conn.cursor()
                update_query ="""UPDATE userrs SET age=%s,phone=%s WHERE id=%s"""
                cur.execute(update_query,(self.age,self.phone,userrs_id))
                conn.commit()
                cur.close()
                conn.close()


user1=userrs('john','doe','20','+123 456 667 721')
user1.save()

all_userrs = userrs.get_userrs()
print(all_userrs)


user2 ==userrs.get