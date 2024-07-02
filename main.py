import psycopg2

conn = psycopg2.connect(database="new_list",
                        user="postgres",
                        host="localhost",
                        password="1",
                        port="5432")

cur = conn.cursor()

select_all_students_query = """
    select * from students;
    """
cur.execute(select_all_students_query)
rows=cur.fetchall()
for students in rows:
    print (students)

#Xolmamatov Farruh
