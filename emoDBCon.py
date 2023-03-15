import sqlite3 as sql

happy=[]
sad=[]


con=sql.connect("emotions")
Cursor=con.cursor()
rs=Cursor.execute("select * from happy")
for i in rs:
    happy.append(i[1])

rs=Cursor.execute("select * from sad")
for i in rs:
    sad.append(i[1])