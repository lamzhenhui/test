import cx_Oracle
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="orcl")
conn = cx_Oracle.connect(user="scott", password="tiger", dsn=dsn)

cursor = conn.cursor()
cursor.execute("SELECT * FROM emp")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
