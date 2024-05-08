import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("CREATE TABLE IF NOT EXISTS COMPANY\n"
             "         (ID INT PRIMARY KEY     NOT NULL,\n"
             "         NAME           TEXT    NOT NULL,\n"
             "         AGE            INT     NOT NULL,\n"
             "         ADDRESS        CHAR(50),\n"
             "         SALARY         REAL);")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)"
             "VALUES (4, 'David',18,'Tring',20000.00)")

conn.commit()
print("Records inserted")

conn.close()
